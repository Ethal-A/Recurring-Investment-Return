# Disclaimer
**This program is not meant to be, nor should be used as financial/investing advice.** This program is also not entirely accurate being unable to account for dividends, stock splits and more. The program cannot retrieve the latest data on stock prices either.

# Recurring Investment Return
Ever wondered, what would my return be over the course of Y years I invested X amount every Z days?

The following Python Script is used to calculate the return on investment from recurring investments into a single stock over a period of time. The script uses Yahoo Finance statistics and will provide a return on investment from the period provided to the latest Yahoo Finance statistics on that stock. The currency is determined by the exchange of the symbol provided. For example, VAS.AX is Vanguard Australian Shares in the Australian Stock Exchange and will therefore use Australian Dollars. The program has key limitations in that it does not account for dividends. Stock splits within the period specified are not accounted for.

## How to use ReturnCalculator.py
To use ReturnCalculator.py use python to run the script via `python ReturnCalculator.py`. You can provide optional paramters (see below) to configure the script.
```
  -h, --help            show this help message and exit
  --period PERIOD, -p PERIOD
                        Period of recurring investment with valid values being: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd and max
  --interval INTERVAL, -i INTERVAL
                        Days between recurring investment
  --symbol SYMBOL, -s SYMBOL
                        The stock symbol
  --amount AMOUNT, -a AMOUNT
                        The amount of money to be invested each interval
```

## Example
The following is output from the use of the script.
```
$ python ReturnCalculator.py -p 5y -i 28 -s VGS.AX -a 1000
On 2018-07-16 bought 14 of VGS.AX at $69.88, investing $978.25
On 2018-08-23 bought 13 of VGS.AX at $71.59, investing $930.67
On 2018-10-02 bought 13 of VGS.AX at $73.86, investing $960.18
On 2018-11-09 bought 14 of VGS.AX at $69.91, investing $978.67
On 2018-12-19 bought 15 of VGS.AX at $64.58, investing $968.70
On 2019-02-01 bought 14 of VGS.AX at $67.74, investing $948.29
On 2019-03-13 bought 13 of VGS.AX at $71.58, investing $930.48
On 2019-04-24 bought 13 of VGS.AX at $74.66, investing $970.64
On 2019-06-04 bought 13 of VGS.AX at $71.60, investing $930.74
On 2019-07-15 bought 13 of VGS.AX at $76.00, investing $988.00
On 2019-08-22 bought 13 of VGS.AX at $76.30, investing $991.90
On 2019-10-01 bought 12 of VGS.AX at $78.32, investing $939.78
On 2019-11-08 bought 12 of VGS.AX at $79.53, investing $954.30
On 2019-12-18 bought 12 of VGS.AX at $82.56, investing $990.72
On 2020-01-31 bought 11 of VGS.AX at $85.69, investing $942.64
On 2020-03-11 bought 13 of VGS.AX at $75.41, investing $980.33
On 2020-04-22 bought 13 of VGS.AX at $74.20, investing $964.60
On 2020-06-01 bought 12 of VGS.AX at $77.99, investing $935.82
On 2020-07-10 bought 12 of VGS.AX at $77.42, investing $928.98
On 2020-08-19 bought 12 of VGS.AX at $79.85, investing $958.14
On 2020-09-28 bought 12 of VGS.AX at $80.12, investing $961.38
On 2020-11-05 bought 12 of VGS.AX at $81.35, investing $976.26
On 2020-12-15 bought 11 of VGS.AX at $83.89, investing $922.74
On 2021-01-28 bought 11 of VGS.AX at $84.33, investing $927.58
On 2021-03-09 bought 11 of VGS.AX at $85.94, investing $945.39
On 2021-04-20 bought 10 of VGS.AX at $91.08, investing $910.85
On 2021-05-28 bought 10 of VGS.AX at $92.78, investing $927.75
On 2021-07-08 bought 10 of VGS.AX at $97.52, investing $975.20
On 2021-08-17 bought 9 of VGS.AX at $101.93, investing $917.37
On 2021-09-24 bought 9 of VGS.AX at $102.17, investing $919.53
On 2021-11-03 bought 9 of VGS.AX at $102.84, investing $925.56
On 2021-12-13 bought 9 of VGS.AX at $107.06, investing $963.50
On 2022-01-25 bought 9 of VGS.AX at $100.33, investing $902.93
On 2022-03-07 bought 10 of VGS.AX at $92.67, investing $926.75
On 2022-04-14 bought 10 of VGS.AX at $95.71, investing $957.05
On 2022-05-27 bought 10 of VGS.AX at $92.33, investing $923.25
On 2022-07-07 bought 11 of VGS.AX at $90.00, investing $990.05
On 2022-08-16 bought 10 of VGS.AX at $96.67, investing $966.65
On 2022-09-26 bought 11 of VGS.AX at $88.80, investing $976.80
On 2022-11-03 bought 10 of VGS.AX at $93.43, investing $934.30
On 2022-12-13 bought 10 of VGS.AX at $94.77, investing $947.70
On 2023-01-25 bought 10 of VGS.AX at $92.73, investing $927.30
On 2023-03-07 bought 10 of VGS.AX at $98.37, investing $983.65
On 2023-04-18 bought 9 of VGS.AX at $100.67, investing $906.03
On 2023-05-29 bought 9 of VGS.AX at $104.37, investing $939.33

Began buying VGS.AX stock on 2018-07-16 with an interval of 28 days per investment of $1,000.00 and sold all stock on 2023-07-07 for a price of $105.02
Amount of money that was not invested (cannot buy portion of a stock in this model): $2,273.28
Amount of money that was invested: $42,726.72
The total value of all investments: $53,455.18
The total gain from investments: $10,728.46
Percentage gain from investments: 25.11%
```