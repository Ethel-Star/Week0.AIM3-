def convert_bytes_to_mb(bytes_value):
    return bytes_value / (1024 * 1024)

def save_dataframe_to_csv(df, file_name):
    df.to_csv(file_name, index=False)
