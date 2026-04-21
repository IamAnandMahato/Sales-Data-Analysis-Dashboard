# 📊 Advanced Sales Analytics Dashboard

🚀 An end-to-end **Sales Data Analysis & Prediction System** built using modern data tools, featuring **interactive dashboards, machine learning, database integration, API connectivity, and authentication**.

---

## 🔥 Key Features

* 📈 **Interactive Dashboard** (Streamlit + Plotly)
* 🤖 **Machine Learning Model** (Sales Prediction using Linear Regression)
* 🗄️ **Database Integration** (MySQL)
* 🌐 **Live API Data Fetching**
* 🔐 **User Authentication System** (Login/Signup)
* 📊 **Real-time Filters & KPI Metrics**
* ☁️ **Cloud Deployment Ready**

---

## 🧠 Tech Stack

| Category         | Technologies Used |
| ---------------- | ----------------- |
| Frontend         | Streamlit         |
| Backend          | Python            |
| Data Analysis    | Pandas            |
| Visualization    | Plotly            |
| Machine Learning | Scikit-learn      |
| Database         | MySQL             |
| API Integration  | Requests          |
| Version Control  | Git               |

---

## 📁 Project Structure

```
sales-dashboard/
│
├── src/
│   ├── app.py
│   ├── auth.py
│   ├── db.py
│   ├── ml_model.py
│   └── api_data.py
│
├── data/
│   └── sales_data.csv
│
├── config/
│   └── config.py
│
├── assets/
│   └── dashboard.png
│
├── .streamlit/
│   └── config.toml
│
├── run.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dashboard Preview

![Dashboard Screenshot](assets/dashboard.png)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/sales-dashboard.git
cd sales-dashboard
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure Database

Update `config/config.py`:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
    "database": "sales_db"
}
```

---

### 4️⃣ Run the Application

```bash
streamlit run run.py
```

---

## 🤖 Machine Learning

* Model Used: **Linear Regression**
* Inputs: Day, Quantity
* Output: Predicted Sales

✔ Enables data-driven decision making
✔ Helps forecast future sales trends

---

## 🌐 API Integration

* Fetches real-time data from external APIs
* Can be extended to IoT or live business systems

---

## 🔐 Authentication System

* Secure login & signup functionality
* Password hashing using SHA-256
* SQLite-based user storage

---

## 📈 Business Insights Provided

* Sales trends over time
* Region-wise performance
* Category-wise analysis
* Profit vs Sales relationship

---

## ☁️ Deployment

You can deploy this project on:

* Streamlit Cloud
* AWS EC2 + RDS
* Docker (optional)

---

## 💼 Resume Description

**Developed an end-to-end Sales Analytics Dashboard with machine learning-based prediction, real-time data integration, and secure authentication, enabling actionable business insights and improved decision-making.**

---

## 🔮 Future Enhancements

* 📊 Advanced forecasting (ARIMA / LSTM)
* 📱 Mobile app integration
* 🔔 Real-time alerts & notifications
* 🌍 Multi-user role-based access

---

## 👨‍💻 Author

**Anand Mahato**
B.Tech CSE (2026)

---

## ⭐ Show Your Support

If you like this project:

* ⭐ Star this repository
* 🍴 Fork it
* 🔗 Share with others

---
