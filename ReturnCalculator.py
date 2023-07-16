# Useful links:
# yfinance documentation: https://pypi.org/project/yfinance/
# yfinance Ticker documentation: https://github.com/ranaroussi/yfinance/wiki/Ticker#history

import yfinance as yf
import datetime

# Define functions for later
def format_dollar(dol: float) -> str:
    if dol < 0:
        dol = abs(dol)
        return '-${:,.2f}'.format(dol)
    else:
        return '${:,.2f}'.format(dol)

def print_price_error(date: datetime.date, price: float) -> None:
    print('Could not invest on {date} due to price being {price}.'.format(date=date, price=format_dollar(price)))

def print_purchase(date: datetime.date, symbol: str, price: float, quantity: int) -> None:
    value = format_dollar(price*quantity)
    price = format_dollar(price)
    print('On {date} bought {number} of {symbol} at {price}, investing {value}'.format(
        date=date,
        number=quantity,
        symbol=symbol,
        price=price,
        value=value))

# Input parameters
symbol = 'VGS.AX'
period = '5y'
interval = 28 # Days
amount = 1000 # Amount to be invested per interval

# Get symbol data
hist = yf.Ticker(symbol).history(period)            # Retrieves pd.DataFrame
hist['avg'] = hist[['High', 'Low']].mean(axis=1)    # Get every nth average value between high and low
intervals = hist.iloc[0::interval, :]               # Investment dates
intervals = intervals['avg'].reset_index()          # This makes the date columns accessible and now we are just focusing on date and avg

# Get values to assist in calculation
start_date = intervals.iloc[0, 0].date()
end_date = intervals.iloc[-1, 0].date()
last_price = intervals.iloc[-1, 1]
intervals.drop(intervals.tail(1).index, inplace=True) # Will not be purchasing stocks on the last day, only selling

# Conduct calculations
invested = 0
not_invested = 0
portfolio_value = 0
portfolio_gain = 0
for i in range(len(intervals)):
    date = intervals.iloc[i, 0].date()
    price = intervals.iloc[i, 1]

    # Error handling
    if price <= 0:
        not_invested += amount
        print_price_error(date, price)
        continue
    
    quantity = int(amount // price)                                     # Quantity of stock to be purchased (rounded to negative infinity)
    invested += quantity * price                                        # Amount that was invested
    not_invested += amount - quantity * price                           # Amount that was not invested
    sale_value = quantity * price * (1 + (last_price - price)/price)    # Value of purchase upon sale at the end of the period provided.
    portfolio_value += sale_value                                       # The value of the portfolio at the end
    portfolio_gain += sale_value - quantity * price                     # The amount gained in value at the end

    print_purchase(date, symbol, price, quantity)

# Print final results.
print('''
Began buying {symbol} stock on {start_date} with an interval of {interval} days per investment of {amount}.
Sold all stock on {end_date} for a price of {last_price}.
Amount of money that was not invested (cannot buy portion of a stock in this model): {not_invested}
Amount of money that was invested: {invested}
The total value of all investments: {portfolio_value}
The total gain from investments: {portfolio_gain}
Percentage gain from investments: {portfolio_percentage_gain}%
'''.format(
symbol=symbol,
start_date=start_date,
interval=interval,
amount=format_dollar(amount),
end_date=end_date,
last_price=format_dollar(last_price),
not_invested=format_dollar(not_invested),
invested=format_dollar(invested),
portfolio_value=format_dollar(portfolio_value),
portfolio_gain=format_dollar(portfolio_gain),
portfolio_percentage_gain=round(100 * (portfolio_value - invested)/invested, 2)))