import pandas as pd
from sklearn.linear_model import LinearRegression

def train_model(df):
    df = df.copy()

    df['Date'] = pd.to_datetime(df['Date'])
    df['Day'] = df['Date'].dt.day

    X = df[['Day', 'Quantity']]
    y = df['Sales']

    model = LinearRegression()
    model.fit(X, y)

    return model

def predict_sales(model, day, quantity):
    prediction = model.predict([[day, quantity]])
    return float(prediction[0])
