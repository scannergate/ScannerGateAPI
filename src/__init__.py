import requests

class ScannerGateAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.scannergate.com/v1"

    def _make_request(self, endpoint, params=None):
        headers = {
            "X-API-KEY": self.api_key
        }
        response = requests.get(f"{self.base_url}/{endpoint}", headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    # Market Data
    def get_market_data(self, symbol, interval):
        params = {"symbol": symbol, "interval": interval}
        return self._make_request("market/ticker", params)

    # Historical Data
    def get_historical_data(self, symbol, interval, start_time, end_time):
        params = {
            "symbol": symbol,
            "interval": interval,
            "startTime": start_time,
            "endTime": end_time
        }
        return self._make_request("market/klines", params)

    # Whale Alerts
    def get_whale_alerts(self, min_amount, chain, timeframe):
        params = {
            "minAmount": min_amount,
            "chain": chain,
            "timeframe": timeframe
        }
        return self._make_request("whales/transactions", params)

    # Social Sentiment
    def get_social_sentiment(self, symbol, sources, timeframe):
        params = {
            "symbol": symbol,
            "sources": sources,
            "timeframe": timeframe
        }
        return self._make_request("social/sentiment", params)

    # Token Analytics
    def get_token_analytics(self, address, chain, metrics):
        params = {
            "address": address,
            "chain": chain,
            "metrics": metrics
        }
        return self._make_request("token/analytics", params)

    # Market Pairs
    def get_market_pairs(self, base_asset, quote_asset, limit=100):
        params = {
            "baseAsset": base_asset,
            "quoteAsset": quote_asset,
            "limit": limit
        }
        return self._make_request("market/pairs", params)

    # Price Predictions
    def get_price_predictions(self, symbol, timeframe, confidence=False):
        params = {
            "symbol": symbol,
            "timeframe": timeframe,
            "confidence": confidence
        }
        return self._make_request("ai/predictions", params)

    # DEX Analytics
    def get_dex_analytics(self, dex, pair, metrics):
        params = {
            "dex": dex,
            "pair": pair,
            "metrics": metrics
        }
        return self._make_request("dex/analytics", params)

    # Gas Tracker
    def get_gas_tracker(self, network, priority):
        params = {
            "network": network,
            "priority": priority
        }
        return self._make_request("network/gas", params)
