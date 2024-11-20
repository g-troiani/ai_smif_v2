# test_data_retrieval.py
from components.data_management_module.data_manager import DataManager
from datetime import datetime
import os
import pandas as pd

# Setup
if not os.path.exists('data'):
    os.makedirs('data')

# Create test tickers file
pd.DataFrame({'ticker': ['AAPL']}).to_csv('data/tickers.csv', index=False)

# Test
try:
    print("Initializing DataManager...")
    dm = DataManager()
    
    print("\nFetching historical data...")
    # First fetch historical data
    dm.fetch_historical_data()
    
    print("\nRetrieving data for backtest...")
    data = dm.get_backtrader_data(
        ticker='AAPL',
        start_date=datetime(2020, 1, 1),
        end_date=datetime(2020, 12, 31)
    )
    
    if data.empty:
        print("\nNo data found. Check if:")
        print("1. Alpaca API credentials are set correctly")
        print("2. Database is initialized properly")
        print("3. Historical data was fetched successfully")
    else:
        print("\nData retrieved successfully:")
        print("\nShape:", data.shape)
        print("\nColumns:", data.columns.tolist())
        print("\nFirst few rows:")
        print(data.head())

except Exception as e:
    print(f"Error: {e}")
    import traceback
    print(traceback.format_exc())

finally:
    # Cleanup
    if os.path.exists('data/tickers.csv'):
        os.remove('data/tickers.csv')