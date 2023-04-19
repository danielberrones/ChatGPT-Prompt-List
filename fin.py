import yfinance as yf

def get_stock_info(ticker):
    """Fetch stock data using yfinance and return basic information."""
    stock = yf.Ticker(ticker)
    info = stock.info
    if info is None:
        print(f"Error: Ticker '{ticker}' not found.")
        return None

    stock_info = {
        'Symbol': info.get('symbol'),
        'Name': info.get('longName'),
        'Exchange': info.get('exchange'),
        'Currency': info.get('currency'),
        'Previous Close': info.get('regularMarketPreviousClose'),
        'Open': info.get('regularMarketOpen'),
        'High': info.get('regularMarketDayHigh'),
        'Low': info.get('regularMarketDayLow'),
        'Close': info.get('regularMarketPreviousClose'),
        'Volume': info.get('regularMarketVolume'),
    }

    return stock_info



print(get_stock_info("msft"))
