import requests
import pandas as pd
from config.config import API_URL

def fetch_api_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()

        df = pd.DataFrame(data)

        # Ensure required columns exist
        required_cols = ["Date", "Region", "Product", "Category", "Sales", "Quantity", "Profit"]
        for col in required_cols:
            if col not in df.columns:
                df[col] = None

        return df

    except Exception as e:
        print("API Error:", e)
        return pd.DataFrame()
