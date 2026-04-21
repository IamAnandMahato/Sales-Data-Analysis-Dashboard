import streamlit as st
import pandas as pd
import plotly.express as px

# Import modules
from src.auth import create_user, login_user
from src.db import fetch_data
from src.ml_model import train_model, predict_sales
from src.api_data import fetch_api_data

# ---------------- MAIN FUNCTION ----------------
def main():

    # Page config
    st.set_page_config(page_title="Advanced Sales Dashboard", layout="wide")

    st.title("📊 Advanced Sales Dashboard")

    # ---------------- SIDEBAR MENU ----------------
    menu = ["Login", "Signup"]
    choice = st.sidebar.selectbox("🔐 Menu", menu)

    # ---------------- SIGNUP ----------------
    if choice == "Signup":
        st.subheader("📝 Create Account")

        new_user = st.text_input("Username")
        new_pass = st.text_input("Password", type="password")

        if st.button("Signup"):
            if new_user and new_pass:
                create_user(new_user, new_pass)
                st.success("✅ Account created successfully!")
            else:
                st.warning("⚠️ Please fill all fields")

    # ---------------- LOGIN ----------------
    elif choice == "Login":
        st.subheader("🔑 Login")

        user = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):

            if login_user(user, password):

                st.success(f"👋 Welcome {user}")

                # ---------------- DATA SOURCE ----------------
                st.sidebar.subheader("📂 Data Source")
                data_source = st.sidebar.radio(
                    "Select Source",
                    ["CSV", "MySQL", "API"]
                )

                # Load data
                if data_source == "CSV":
                    df = pd.read_csv("data/sales_data.csv")

                elif data_source == "MySQL":
                    df = fetch_data()

                else:
                    df = fetch_api_data()

                # Data preprocessing
                df['Date'] = pd.to_datetime(df['Date'])

                # ---------------- FILTERS ----------------
                st.sidebar.subheader("🔍 Filters")

                region = st.sidebar.multiselect(
                    "Region",
                    options=df["Region"].unique(),
                    default=df["Region"].unique()
                )

                category = st.sidebar.multiselect(
                    "Category",
                    options=df["Category"].unique(),
                    default=df["Category"].unique()
                )

                # Apply filters
                filtered_df = df[
                    (df["Region"].isin(region)) &
                    (df["Category"].isin(category))
                ]

                # ---------------- KPI METRICS ----------------
                st.subheader("📈 Key Metrics")

                col1, col2, col3 = st.columns(3)

                col1.metric("💰 Total Sales", f"₹{filtered_df['Sales'].sum():,.0f}")
                col2.metric("📊 Total Profit", f"₹{filtered_df['Profit'].sum():,.0f}")
                col3.metric("📦 Total Quantity", f"{filtered_df['Quantity'].sum():,.0f}")

                # ---------------- CHARTS ----------------

                # Sales Trend
                st.subheader("📅 Sales Trend")
                sales_trend = filtered_df.groupby("Date")["Sales"].sum().reset_index()

                fig1 = px.line(sales_trend, x="Date", y="Sales", markers=True)
                st.plotly_chart(fig1, use_container_width=True)

                # Region-wise Sales
                st.subheader("🌍 Sales by Region")
                region_sales = filtered_df.groupby("Region")["Sales"].sum().reset_index()

                fig2 = px.bar(region_sales, x="Region", y="Sales", color="Region")
                st.plotly_chart(fig2, use_container_width=True)

                # Category-wise Sales
                st.subheader("📦 Sales by Category")
                cat_sales = filtered_df.groupby("Category")["Sales"].sum().reset_index()

                fig3 = px.pie(cat_sales, names="Category", values="Sales")
                st.plotly_chart(fig3, use_container_width=True)

                # Profit vs Sales
                st.subheader("📊 Profit vs Sales Analysis")

                fig4 = px.scatter(
                    filtered_df,
                    x="Sales",
                    y="Profit",
                    size="Quantity",
                    color="Category",
                    hover_data=["Product"]
                )

                st.plotly_chart(fig4, use_container_width=True)

                # ---------------- MACHINE LEARNING ----------------
                st.subheader("🤖 Sales Prediction (ML Model)")

                model = train_model(filtered_df)

                colA, colB = st.columns(2)

                day = colA.slider("📅 Select Day of Month", 1, 31, 15)
                quantity = colB.slider("📦 Select Quantity", 1, 20, 5)

                if st.button("🔮 Predict Sales"):
                    prediction = predict_sales(model, day, quantity)
                    st.success(f"💰 Predicted Sales: ₹{round(prediction, 2)}")

                # ---------------- DATA TABLE ----------------
                st.subheader("📋 Filtered Data")
                st.dataframe(filtered_df, use_container_width=True)

            else:
                st.error("❌ Invalid username or password")


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    main()
