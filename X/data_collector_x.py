import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

class DataPreprocessor:
    def __init__(self):
        self.scaler = MinMaxScaler()

    def clean_data(self, df):
        # Remove any rows with NaN values
        df = df.dropna()
        # Convert time to numeric for differential calculations
        df['Time'] = pd.to_datetime(df['Time'])
        df['Time'] = (df['Time'] - df['Time'].min()) / np.timedelta64(1, 'D')
        return df

    def normalize_data(self, df):
        """
        Normalize the data using MinMaxScaler.
        """
        features = self.scaler.fit_transform(df[['Price', 'Time']])
        df[['Price', 'Time']] = features
        return df

    def create_features(self, df):
        """
        Create additional features like moving averages, price changes, etc.
        """
        # Example: 7-day moving average
        df['MA7'] = df['Price'].rolling(window=7).mean()
        # Price change from previous day
        df['Price_Change'] = df['Price'].diff(1)
        # Normalize the new features
        new_features = self.scaler.fit_transform(df[['MA7', 'Price_Change']])
        df[['MA7', 'Price_Change']] = new_features
        return df

    def preprocess(self, df):
        df = self.clean_data(df)
        df = self.normalize_data(df)
        df = self.create_features(df)
        return df
