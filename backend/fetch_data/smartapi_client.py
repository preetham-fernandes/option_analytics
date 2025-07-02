# backend/fetch/smartapi_fetcher.py

from nifty_vix_scraper.backend.fetch_data.smartapi_login import smartapi_login
from datetime import datetime

def fetch_option_data():
    session = smartapi_login()
    if not session:
        return []

    obj = session['client']
    index_symbol = "NIFTY"
    strike_prices = [125500]
    data_points = []

    for strike in strike_prices:
        for opt_type in ["CE", "PE"]:
            symbol = f"{index_symbol}{strike}{opt_type}"
            try:
                ltp_data = obj.ltpData(
                    exchange="NFO",
                    tradingsymbol=symbol,
                    symboltoken="56843",  # Replace with actual token
                    variety="NORMAL"
                )
                ltp = float(ltp_data['data']['ltp'])
                data_points.append({
                    "timestamp": datetime.now(),
                    "symbol": index_symbol,
                    "strike_price": strike,
                    "option_type": opt_type,
                    "ltp": ltp
                })
            except Exception as e:
                print(f"❌ Error fetching {symbol}: {e}")
    
    return data_points

if __name__ == "__main__":
    data = fetch_option_data()
    print("Fetched Option Data:")
    for entry in data:
        print(entry)
