# backend/fetch/vix_fetcher.py

import yfinance as yf
from datetime import datetime

def fetch_vix_value():
    vix = yf.Ticker("^INDIAVIX")
    data = vix.history(period="1d", interval="1m")
    
    if data.empty:
        print("❌ VIX data not available")
        return None

    # Latest available value
    latest = data.iloc[-1]
    return {
        "timestamp": latest.name.to_pydatetime(),
        "vix_value": float(latest["Close"])
    }

if __name__ == "__main__":
    print(fetch_vix_value())
