# libs
import ta
import yfinance as yf
from datetime import datetime
from tabulate import tabulate
from colorama import Fore, Style
# libs

#INIT

#INIT

# Date Entry | Date Format YYYY-MM-DD
start_date = "2022-03-04"
#start_date = input("[Enter Start Date | Format YYYY-MM-DD] : ")
current_date = datetime.now().strftime('%Y-%m-%d')
# Date Entry

# Finding Stock Signal for Single Stock
def find_single_stock_signal():
    stock_code = "ITC.NS"
    #stock_code = input("[Enter Stock Code] : ")
    try:
        data = yf.download(stock_code, start=start_date, end=current_date)
        

        if len(data) < 14:
            print("Not enough data for" + stock_code)
        
        else:
            #calculation of Signals
            rsi = ta.momentum.RSIIndicator(data['Close'], window=14).rsi().iloc[-1]
            upper_band = ta.volatility.BollingerBands(data['Close']).bollinger_hband().iloc[-1]
            lower_band = ta.volatility.BollingerBands(data['Close']).bollinger_lband().iloc[-1]
            macd = ta.trend.MACD(data['Close']).macd().iloc[-1]
            signal = ta.trend.MACD(data['Close']).macd_signal().iloc[-1]
            #calculation of signals 

            #algo for determining buy,sell or neutral signal
            macd_signal = 'BUY' if macd > signal else 'SELL' if macd < signal else 'NEUTRAL'
            rsi_signal = 'BUY' if rsi < 30 else 'SELL' if rsi > 70 else 'NEUTRAL'
            bollinger_signal = 'BUY' if data['Close'].iloc[-1] < lower_band else 'SELL' if data['Close'].iloc[-1] > upper_band else 'NEUTRAL'
            #algo for determining buy,sell or neutral signal
           
            
            #display the result in table
            headers = ["Stock", stock_code]
            table_data = [
                ["Latest Date of Data Acquired", data.index[-1].strftime('%Y-%m-%d')],
                ["Latest Stock Price", data['Close'].iloc[-1]],
                ["Latest MACD Value", f"macd: {macd} | signal: {signal}"],
                ["Latest RSI Value", rsi],
                ["Latest BB Value", f"lower_band: {lower_band} | upper_band: {upper_band}"],
                ["MACD Signal", macd_signal],
                ["RSI Signal", rsi_signal],
                ["Bollinger Bands Signal", bollinger_signal]
            ]
            
            print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
    
    except:
        print("Error fetching data for " + stock_code)

    
# Finding Stock Signal for Single Stock
find_single_stock_signal()