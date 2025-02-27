# ScannerGate API Python Wrapper

This is a Python wrapper for the ScannerGate API that provides access to various market data, whale alerts, social sentiment, and more.

## Installation

To install this package, you can use pip to install it directly from GitHub:

```bash
pip install git+https://github.com/scannergate/ScannerGateAPI.git
```

## Usage

Once installed, you can import the `ScannerGateAPI` class and start using it to fetch data from the ScannerGate API.

### Example Usage

```python
from ScannerGateAPI import ScannerGateAPI

# Initialize the API client with your API key
api_key = "YOUR_API_KEY"
client = ScannerGateAPI(api_key)

# Get market data for a specific trading pair (BTC/USDT)
market_data = client.get_market_data("BTCUSDT", "1h")
print("Market Data:", market_data)

# Get whale alerts with a minimum transaction amount of 100000 USD
whale_alerts = client.get_whale_alerts(100000, "ETH", "1h")
print("Whale Alerts:", whale_alerts)

# Get token analytics for a specific token address
token_analytics = client.get_token_analytics("0xTokenAddress", "ETH", ["holders", "volume", "liquidity"])
print("Token Analytics:", token_analytics)

# Get price prediction for BTC
price_prediction = client.get_price_predictions("BTC", "24h", confidence=True)
print("Price Prediction:", price_prediction)
```


## API Methods

- `get_market_data(symbol, interval)`
- `get_historical_data(symbol, interval, start_time, end_time)`
- `get_whale_alerts(min_amount, chain, timeframe)`
- `get_social_sentiment(symbol, sources, timeframe)`
- `get_token_analytics(address, chain, metrics)`
- `get_market_pairs(base_asset, quote_asset, limit)`
- `get_price_predictions(symbol, timeframe, confidence)`
- `get_dex_analytics(dex, pair, metrics)`
- `get_gas_tracker(network, priority)`

For more details, refer to the API documentation: [ScannerGate API Docs](https://www.scannergate.com/)
