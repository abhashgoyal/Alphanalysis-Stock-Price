# Test code to verify stock data fetching
import yfinance as yf

# Test with a single stock
test_ticker = "RELIANCE.NS"
data = yf.download(test_ticker, start="2024-01-01", end="2024-01-10")
print(data.head())