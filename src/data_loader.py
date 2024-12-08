import pandas as pd

def load_datasets():
    # Define file paths for each dataset
    benin_path = r'C:\\Users\\ethio\\Desktop\\Tenx.AIM3\\Week0\\Week0.AIM3-\\data\\benin-malanville.csv'
    sierra_leone_path = r'C:\\Users\\ethio\\Desktop\\Tenx.AIM3\\Week0\\Week0.AIM3-\\data\\sierraleone-bumbuna.csv'
    togo_path = r'C:\\Users\\ethio\\Desktop\\Tenx.AIM3\\Week0\\Week0.AIM3-\\data\\togo-dapaong_qc.csv'

    # Load datasets
    dt_ben = pd.read_csv(benin_path)
    dt_sier = pd.read_csv(sierra_leone_path)
    dt_togo = pd.read_csv(togo_path)

    return dt_ben, dt_sier, dt_togo

