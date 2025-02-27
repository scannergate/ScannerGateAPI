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
