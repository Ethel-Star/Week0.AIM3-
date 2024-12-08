# tests/test_analyze_data.py

import unittest
from src.data_loader import load_and_preprocess_data

class TestDataAnalysis(unittest.TestCase):

    def test_load_and_preprocess_data(self):
        # Replace with your actual file path for testing
        test_file = 'C:\\Users\\ethio\\Desktop\\Tenx.AIM3\\Week0\\Week0.AIM3-\\data\\benin-malanville.csv'
        df = load_and_preprocess_data(test_file)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue(df.index.is_all_dates)  # Ensures 'Timestamp' is set as index
        self.assertTrue('GHI' in df.columns)  # Check if 'GHI' column exists

if __name__ == "__main__":
    unittest.main()
