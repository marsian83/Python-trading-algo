import requests
import pandas as pd
import plotly.graph_objects as go

API_KEY = "Enter your api key here"

class ScriptData:
    def __init__(self):
        self.api_key = API_KEY
        self.data = {}
        self.df = {}

    def fetch_intraday_data(self, script):
        api_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={script}&interval=5min&apikey={self.api_key}"
        response = requests.get(api_url)
        data = response.json()

        intraday_data = data["Time Series (5min)"]

        self.data[script] = intraday_data

    def convert_intraday_data(self, script):
        formattedData = {}
        i = 0
        for timestamp, data_dict in self.data[script].items():
            formattedData[str(i)] = {
                "timestamp": timestamp,
                "open": data_dict["1. open"],
                "high": data_dict["2. high"],
                "low": data_dict["3. low"],
                "close": data_dict["4. close"],
                "volume": data_dict["5. volume"]
            }
            i += 1

        dataframe = pd.DataFrame.from_dict(formattedData, orient="index", columns=[
            "timestamp", "open", "high", "low", "close", "volume"])

        self.df[script] = dataframe

    def __getitem__(self, key):
        return self.df[key]

    def __setitem__(self, key, value):
        self.df[key] = value

    def __contains__(self, item):
        return item in self.df


def indicator1(df, timeperiod):
    moving_avg = df['close'].rolling(timeperiod).mean()
    result = pd.DataFrame(
        {'timestamp': df['timestamp'], 'indicator': moving_avg})
    return result


class Strategy:
    def __init__(self, script):
        self.script = script
        self.script_data = ScriptData()
        self.signals = None

    def get_script_data(self):
        self.script_data.fetch_intraday_data(self.script)
        self.script_data.convert_intraday_data(self.script)
        self.df = self.script_data[self.script]

    def compute_indicator_data(self, timeperiod):
        self.indicator_data = indicator1(self.df, timeperiod)

    def get_signals(self):
        self.signals = pd.DataFrame(columns=['timestamp', 'signal'])

        for i in range(1, len(self.df)):

            indicator = float(self.indicator_data['indicator'][i])
            close = float(self.df['close'][i])
            indicator_prev = float(self.indicator_data['indicator'][i-1])
            close_prev = float(self.df['close'][i-1])

            if indicator > close and indicator_prev <= close_prev:
                self.signals.loc[i, 'timestamp'] = self.df['timestamp'][i]
                self.signals.loc[i, 'signal'] = 'BUY'
            elif indicator < close and indicator_prev >= close_prev:
                self.signals.loc[i, 'timestamp'] = self.df['timestamp'][i]
                self.signals.loc[i, 'signal'] = 'SELL'
            else:
                self.signals.loc[i, 'timestamp'] = self.df['timestamp'][i]
                self.signals.loc[i, 'signal'] = 'NO_SIGNAL'

        return (self.signals[self.signals['signal'] != 'NO_SIGNAL'])

    def plot_strategy(self):
        candlestick = go.Candlestick(
            x=self.df['timestamp'],
            open=self.df["open"],
            high=self.df["high"],
            low=self.df["low"],
            close=self.df["close"],
            name="Historical Data"
        )

        indicator_line = go.Scatter(
            x=self.indicator_data['timestamp'],
            y=self.indicator_data['indicator'],
            name='SMA',
            line_color='gray'
        )

        fig = go.Figure(data=[candlestick, indicator_line])
        fig.update_layout(
            xaxis=go.layout.XAxis(
                dtick=10,
                tickmode="array",
                tickvals=self.indicator_data['timestamp'],
                ticktext=self.indicator_data['timestamp'],
                tickangle=90,
                tickfont=dict(size=10)
            )
        )
        fig.show()


strategy = Strategy('GOOGL')
strategy.get_script_data()
strategy.compute_indicator_data(5)
strategy.get_signals()
strategy.plot_strategy()
