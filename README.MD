# Stock Trading Strategy

This repository contains code for a stock trading strategy based on intraday data from the Alpha Vantage API.

## Getting Started

To use this code, you will need an API key from Alpha Vantage. Once you have obtained an API key, enter it in the `API_KEY` variable at the top of the `script.py` file.

## Usage

The main class in this repository is the `Strategy` class, which is defined in the `script.py` file. To use the `Strategy` class, you will need to instantiate it and pass it the stock symbol for which you want to retrieve data.

```python
from script import Strategy

strategy = Strategy('AAPL')
```
Once you have instantiated the Strategy class, you can use the following methods to retrieve and analyze data for the given stock:

get_script_data: retrieves intraday data for the stock and stores it in the df attribute of the Strategy instance.
compute_indicator_data: calculates the simple moving average of the closing price for the stock and stores the resulting data in the indicator_data attribute of the Strategy instance.
get_signals: generates trading signals based on the data stored in the df and indicator_data attributes of the Strategy instance and stores the resulting data in the signals attribute of the Strategy instance.
```python
strategy.get_script_data()
strategy.compute_indicator_data(50)
signals = strategy.get_signals()
```

Finally, you can use the plot_strategy method to visualize the stock data and trading signals using the plotly library:
```python
strategy.plot_strategy()
```

Dependencies
This code relies on the following Python libraries:

>requests

>pandas

>plotly


Ensure that these libraries are installed before running the code.