import yfinance as yf
import matplotlib.pyplot as plt

def plot_stock_history(ticker_symbol, period="6mo"):
    # Download historical data for the given ticker
    stock = yf.Ticker(ticker_symbol)
    hist = stock.history(period=period)

    if hist.empty:
        print(f"No data found for ticker: {ticker_symbol}")
        return

    # Plot the closing price
    plt.figure(figsize=(12,6))
    plt.plot(hist.index, hist['Close'], label='Close Price')
    plt.title(f'{ticker_symbol} Stock Price History ({period})')
    plt.xlabel('Date')
    plt.ylabel('Close Price (USD)')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Stock Market Data Visualization")
    ticker = input("Enter the stock ticker symbol (e.g., AAPL, MSFT): ").upper()
    period = input("Enter the period (e.g., 1mo, 3mo, 6mo, 1y, 5y) [default=6mo]: ").strip() or "6mo"
    plot_stock_history(ticker, period)