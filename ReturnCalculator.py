import yfinance as yf
import pandas as pd
import sys

# Input parameters
symbol = 'IVV.AX'
period= '5y'
invest_interval = 28 # Days
recur_invest = 1000

# Error testing
interval_opts = {}  # TODO
if recur_invest <= 0:
    print('Error: Invalid amount of money being invested.', file=sys.stderr)
    sys.exit(1) # Abort because of error.

# Get symbol data
hist = yf.Ticker(symbol).history(period) # Retrieves pd.DataFrame


