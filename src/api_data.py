import requests
import pandas as pd
API_URL = "https://api.mocki.io/v1/0a1b2c3d"

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
