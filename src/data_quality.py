import numpy as np
from scipy import stats
import pandas as pd
def check_data_quality(df, columns):
    # Missing values
    missing_values = df.isnull().sum()
    print("Missing values per column:\n", missing_values)

    # Negative values check
    for column in columns:
        negative_values = df[df[column] < 0].shape[0]
        print(f"Negative values in {column}: {negative_values}")

    # Checking for outliers using Z-scores
    z_scores = np.abs(stats.zscore(df[columns].select_dtypes(include=[np.number])))
    
    # Outliers are defined as points where Z-score > 3
    outliers = np.where(z_scores > 3)
    print("Outliers detected at positions (row, column):\n", outliers)
    
    # Count the number of outliers
    outliers_count = (z_scores > 3).sum(axis=0)
    print("Number of outliers in each column:\n", outliers_count)
def preprocess_data(df):
    # Check if 'Timestamp' exists in the DataFrame
    if 'Timestamp' not in df.columns:
        raise KeyError("The 'Timestamp' column is missing from the DataFrame.")

    # Convert 'Timestamp' to datetime
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

    # Remove rows with missing or invalid 'Timestamp'
    if df['Timestamp'].isna().any():
        print(f"Dropping rows with invalid 'Timestamp' values.")
        df = df.dropna(subset=['Timestamp'])

    # Set 'Timestamp' as the index
    df.set_index('Timestamp', inplace=True)

    return df
