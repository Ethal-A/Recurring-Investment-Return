# Recurring Investment Return
Ever wondered, whatw ould my return be over the course of Y years I invested X amount every Z days?

The following Python Script is used to calculate the return on investment from recurring investments into a single stock over a period of time. The script uses Yahoo Finance statistics and will provide a return on investment from the period provided to the latest Yahoo Finance statistics on that stock. The currency is determined by the exchange of the symbol provided. For example, VAS.AX is Vanguard Australian Shares in the Australian Stock Exchange and will therefore use Australian Dollars. The program has key limitations in that it does not account for dividends. Stock splits within the period specified are not accounted for.

## How to use ReturnCalculator.py
To use ReturnCalculator.py use python to run the script via `python ReturnCalculator.py`. You can provide optional paramters (see below) to configure the script.
```
  -h, --help            show this help message and exit
  --period PERIOD, -p PERIOD
                        Period of recurring investment. Valid values: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
  --interval INTERVAL, -i INTERVAL
                        Days between recurring investment
  --symbol SYMBOL, -s SYMBOL
                        The stock symbol.
  --amount AMOUNT, -a AMOUNT
                        The amount of money to be invested each interval.
```