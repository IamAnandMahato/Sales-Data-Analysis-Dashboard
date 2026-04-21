import mysql.connector
import pandas as pd
from config.config import DB_CONFIG

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def fetch_data():
    conn = get_connection()
    query = "SELECT * FROM sales"
    df = pd.read_sql(query, conn)
    conn.close()
    return df
