# Stock Trading Strategy

This repository contains code for a stock trading strategy based on intraday data from the Alpha Vantage API.
The repository comes with a jupyter notebook file and also a python script.

## Getting Started

To use this code, you will need an API key from Alpha Vantage. Once you have obtained an API key, enter it in the `API_KEY` variable at the top of the `main` file (main.ipynb or main.py depending upon the way you want to execute the code).

## Usage

The Jupytner notebook file is ready to go and automatically installs all the requirements as specified in `requirements.txt` it also upgrades the nbformat module automatically which is required to display the graph properly.

>NOTE : Ignore the error/warning squiggles on the pip commands. The code works perfectly fine and they are just to ensure that you are installing the requirements within the correct environment

The main class in this repository is the `Strategy` class, which is defined in the `script.py` file. To use the `Strategy` class, you will need to instantiate it and pass it the stock symbol for which you want to retrieve data.

```python
strategy = Strategy('AAPL')
```
Once you have instantiated the Strategy class, you can use the following methods to retrieve and analyze data for the given stock:

>**get_script_data:** retrieves intraday data for the stock and stores it in the df attribute of the Strategy instance.

>**compute_indicator_data:** calculates the simple moving average of the closing price for the stock and stores the resulting data in the indicator_data attribute of the Strategy instance.

>**get_signals:** generates trading signals based on the data stored in the df and indicator_data attributes of the Strategy instance and stores the resulting data in the signals attribute of the Strategy instance.

Example : 
```python
strategy.get_script_data('AAPL')
strategy.compute_indicator_data(5)
signals = strategy.get_signals()
```

Finally, you can use the plot_strategy method to visualize the stock data and trading signals using the plotly library which is recommended in the pyalgotrading documentations page:
```python
strategy.plot_strategy()
```