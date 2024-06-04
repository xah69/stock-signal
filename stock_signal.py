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

# Find Stock Signal for all sector and stocks mentionrd in the list 
# Lists of stocks for different sectors
nifty_fmcg_stocks = [
    ('Hindustan Unilever Ltd', 'HINDUNILVR.NS'),
    ('Nestlé India Ltd', 'NESTLEIND.NS'),
    ('ITC Ltd', 'ITC.NS'),
    ('Britannia Industries Ltd', 'BRITANNIA.NS'),
    ('Colgate-Palmolive (India) Ltd', 'COLPAL.NS'),
    ('Godrej Consumer Products Ltd', 'GODREJCP.NS'),
    ('Marico Ltd', 'MARICO.NS'),
    ('Dabur India Ltd', 'DABUR.NS'),
    ('United Spirits Ltd', 'MCDOWELL-N.NS'),
    ('Emami Ltd', 'EMAMILTD.NS')
]

nifty_consumer_durables_stocks = [
    ('Titan Company Ltd', 'TITAN.NS'),
    ('Voltas Ltd', 'VOLTAS.NS'),
    ('Whirlpool of India Ltd', 'WHIRLPOOL.NS'),
    ('Symphony Ltd', 'SYMPHONY.NS'),
    ('TTK Prestige Ltd', 'TTKPRESTIG.NS'),
    ('Crompton Greaves Consumer Electricals Ltd', 'CROMPTON.NS'),
    ('Blue Star Ltd', 'BLUESTARCO.NS'),
    ('Relaxo Footwears Ltd', 'RELAXO.NS'),
    ('VIP Industries Ltd', 'VIPIND.NS'),
    ('Page Industries Ltd', 'PAGEIND.NS')
]

nifty_it_stocks = [
    ('Tata Consultancy Services Ltd', 'TCS.NS'),
    ('Infosys Ltd', 'INFY.NS'),
    ('Wipro Ltd', 'WIPRO.NS'),
    ('HCL Technologies Ltd', 'HCLTECH.NS'),
    ('Tech Mahindra Ltd', 'TECHM.NS'),
    ('Mphasis Ltd', 'MPHASIS.NS'),
    ('MindTree Ltd', 'MINDTREE.NS'),
    ('L&T Infotech Ltd', 'LTI.NS'),
    ('Coforge Ltd', 'COFORGE.NS'),
    ('Tata Elxsi Ltd', 'TATAELXSI.NS')
]

nifty_energy_stocks = [
    ('Reliance Industries Ltd', 'RELIANCE.NS'),
    ('Oil and Natural Gas Corporation Ltd', 'ONGC.NS'),
    ('Indian Oil Corporation Ltd', 'IOC.NS'),
    ('GAIL (India) Ltd', 'GAIL.NS'),
    ('Bharat Petroleum Corporation Ltd', 'BPCL.NS'),
    ('Coal India Ltd', 'COALINDIA.NS'),
    ('Tata Power Company Ltd', 'TATAPOWER.NS'),
    ('Power Grid Corporation of India Ltd', 'POWERGRID.NS'),
    ('NTPC Ltd', 'NTPC.NS'),
    ('Oil India Ltd', 'OIL.NS')
]

nifty_banking_stocks = [
    ('HDFC Bank Ltd', 'HDFCBANK.NS'),
    ('ICICI Bank Ltd', 'ICICIBANK.NS'),
    ('State Bank of India', 'SBIN.NS'),
    ('Kotak Mahindra Bank Ltd', 'KOTAKBANK.NS'),
    ('Axis Bank Ltd', 'AXISBANK.NS'),
    ('IndusInd Bank Ltd', 'INDUSINDBK.NS'),
    ('Bandhan Bank Ltd', 'BANDHANBNK.NS'),
    ('IDFC First Bank Ltd', 'IDFCFIRSTB.NS'),
    ('RBL Bank Ltd', 'RBLBANK.NS'),
    ('Federal Bank Ltd', 'FEDERALBNK.NS')
]

nifty_pharma_stocks = [
    ('Sun Pharmaceutical Industries Ltd', 'SUNPHARMA.NS'),
    ('Dr. Reddy\'s Laboratories Ltd', 'DRREDDY.NS'),
    ('Divi\'s Laboratories Ltd', 'DIVISLAB.NS'),
    ('Cipla Ltd', 'CIPLA.NS'),
    ('Lupin Ltd', 'LUPIN.NS'),
    ('Aurobindo Pharma Ltd', 'AUROPHARMA.NS'),
    ('Biocon Ltd', 'BIOCON.NS'),
    ('Cadila Healthcare Ltd', 'CADILAHC.NS'),
    ('Torrent Pharmaceuticals Ltd', 'TORNTPHARM.NS'),
    ('Alkem Laboratories Ltd', 'ALKEM.NS')
]

nifty_vehicles_stocks = [
    ('Maruti Suzuki India Ltd', 'MARUTI.NS'),
    ('Mahindra & Mahindra Ltd', 'M&M.NS'),
    ('Tata Motors Ltd', 'TATAMOTORS.NS'),
    ('Bajaj Auto Ltd', 'BAJAJ-AUTO.NS'),
    ('Hero MotoCorp Ltd', 'HEROMOTOCO.NS'),
    ('Eicher Motors Ltd', 'EICHERMOT.NS'),
    ('TVS Motor Company Ltd', 'TVSMOTOR.NS'),
    ('Ashok Leyland Ltd', 'ASHOKLEY.NS'),
    ('Motherson Sumi Systems Ltd', 'MOTHERSUMI.NS'),
    ('Balkrishna Industries Ltd', 'BALKRISIND.NS')
]


# Organize stocks by sectors
sectors = {
    'FMCG': nifty_fmcg_stocks,
    'Consumer Durables': nifty_consumer_durables_stocks,
    'IT': nifty_it_stocks,
    'Energy': nifty_energy_stocks,
    'Banking': nifty_banking_stocks,
    'Pharma': nifty_pharma_stocks,
    'Vehicles': nifty_vehicles_stocks,
}


def find_all_stock_signal_listed():
    for sector, sector_stocks in sectors.items():
        for stock_name, stock_code in sector_stocks:
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
        
        
        """    data = yf.download(stock_code, start=start_date, end=current_date)

            if len(data) < 14:
                continue

            rsi = ta.momentum.RSIIndicator(data['Close'], window=14).rsi().iloc[-1]
            upper_band = ta.volatility.BollingerBands(data['Close']).bollinger_hband().iloc[-1]
            lower_band = ta.volatility.BollingerBands(data['Close']).bollinger_lband().iloc[-1]
            macd = ta.trend.MACD(data['Close']).macd().iloc[-1]
            signal = ta.trend.MACD(data['Close']).macd_signal().iloc[-1]

            macd_signal = 'BUY' if macd > signal else 'SELL' if macd < signal else 'NEUTRAL'
            rsi_signal = 'BUY' if rsi < 30 else 'SELL' if rsi > 70 else 'NEUTRAL'
            bollinger_signal = 'BUY' if data['Close'].iloc[-1] < lower_band else 'SELL' if data['Close'].iloc[-1] > upper_band else 'NEUTRAL'
        """
find_all_stock_signal_listed()

# Find Stock Signal for all sector and stocks mentionrd in the list 
