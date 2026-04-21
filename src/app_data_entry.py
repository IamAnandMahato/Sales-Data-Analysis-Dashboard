import streamlit as st
import pandas as pd
import plotly.express as px

from auth import create_user, login_user
from ml_model import train_model, predict_sales
from api_data import fetch_api_data

def main():

    st.set_page_config(page_title="Sales Dashboard", layout="wide")

    st.title("📊 Sales Data Analysis Dashboard")

    # ---------------- AUTH ----------------
    menu = ["Login", "Signup"]
    choice = st.sidebar.selectbox("Menu", menu)

    # ---------------- SIGNUP ----------------
    if choice == "Signup":
        st.subheader("Create Account")

        new_user = st.text_input("Username")
        new_pass = st.text_input("Password", type="password")

        if st.button("Signup"):
            if new_user and new_pass:
                create_user(new_user, new_pass)
                st.success("Account created successfully!")
            else:
                st.warning("Please fill all fields")

    # ---------------- LOGIN ----------------
    elif choice == "Login":
        st.subheader("Login")

        user = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):

            if login_user(user, password):

                st.success(f"Welcome {user} 👋")

                # ---------------- DATA SOURCE ----------------
                st.sidebar.subheader("Data Source")
                data_source = st.sidebar.radio("Select Source", ["CSV", "API"])

                # Load Data
                if data_source == "CSV":
                    file_path = "data/sales_data.csv"
                    df = pd.read_csv(file_path)
                else:
                    df = fetch_api_data()

                if df.empty:
                    st.error("No data available")
                    return

                df['Date'] = pd.to_datetime(df['Date'])

                # ---------------- DATA ENTRY ----------------
                st.subheader("➕ Add New Sales Record")

                with st.form("data_entry_form"):
                    date = st.date_input("Date")
                    region = st.text_input("Region")
                    product = st.text_input("Product")
                    category = st.text_input("Category")
                    sales = st.number_input("Sales", min_value=0)
                    quantity = st.number_input("Quantity", min_value=1)
                    profit = st.number_input("Profit", min_value=0)

                    submit = st.form_submit_button("Add Data")

                    if submit:
                        if data_source == "CSV":
                            new_data = pd.DataFrame([{
                                "Date": date,
                                "Region": region,
                                "Product": product,
                                "Category": category,
                                "Sales": sales,
                                "Quantity": quantity,
                                "Profit": profit
                            }])

                            new_data.to_csv(file_path, mode='a', header=False, index=False)
                            st.success("Data added successfully! Refresh page to see changes.")

                        else:
                            st.warning("Data entry only works with CSV mode.")

                # ---------------- FILTERS ----------------
                st.sidebar.subheader("Filters")

                region_filter = st.sidebar.multiselect(
                    "Region",
                    options=df["Region"].dropna().unique(),
                    default=df["Region"].dropna().unique()
                )

                category_filter = st.sidebar.multiselect(
                    "Category",
                    options=df["Category"].dropna().unique(),
                    default=df["Category"].dropna().unique()
                )

                filtered_df = df[
                    (df["Region"].isin(region_filter)) &
                    (df["Category"].isin(category_filter))
                ]

                # ---------------- METRICS ----------------
                st.subheader("📈 Key Metrics")

                col1, col2, col3 = st.columns(3)

                col1.metric("Total Sales", f"₹{filtered_df['Sales'].sum():,.0f}")
                col2.metric("Total Profit", f"₹{filtered_df['Profit'].sum():,.0f}")
                col3.metric("Total Quantity", f"{filtered_df['Quantity'].sum():,.0f}")

                # ---------------- CHARTS ----------------
                st.subheader("📅 Sales Trend")
                sales_trend = filtered_df.groupby("Date")["Sales"].sum().reset_index()
                fig1 = px.line(sales_trend, x="Date", y="Sales", markers=True)
                st.plotly_chart(fig1, use_container_width=True)

                st.subheader("🌍 Sales by Region")
                region_sales = filtered_df.groupby("Region")["Sales"].sum().reset_index()
                fig2 = px.bar(region_sales, x="Region", y="Sales", color="Region")
                st.plotly_chart(fig2, use_container_width=True)

                st.subheader("📦 Sales by Category")
                cat_sales = filtered_df.groupby("Category")["Sales"].sum().reset_index()
                fig3 = px.pie(cat_sales, names="Category", values="Sales")
                st.plotly_chart(fig3, use_container_width=True)

                st.subheader("📊 Profit vs Sales")
                fig4 = px.scatter(
                    filtered_df,
                    x="Sales",
                    y="Profit",
                    size="Quantity",
                    color="Category",
                    hover_data=["Product"]
                )
                st.plotly_chart(fig4, use_container_width=True)

                # ---------------- ML ----------------
                st.subheader("🤖 Sales Prediction")

                model = train_model(filtered_df)

                day = st.slider("Day", 1, 31, 15)
                quantity = st.slider("Quantity", 1, 20, 5)

                if st.button("Predict"):
                    prediction = predict_sales(model, day, quantity)
                    st.success(f"Predicted Sales: ₹{round(prediction, 2)}")

                # ---------------- TABLE ----------------
                st.subheader("📋 Data Table")
                st.dataframe(filtered_df)

            else:
                st.error("Invalid credentials")

if __name__ == "__main__":
    main()
