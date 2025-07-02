# backend/fetch/smartapi_login.py

from SmartApi.smartConnect import SmartConnect
import pyotp
import os

# Ideally move these to a .env file and load via dotenv
API_KEY = "X2TDF2WQ"
CLIENT_ID = "N225708"
PASSWORD = "2310"
TOTP_SECRET = "AGGVTSMP2IXHCOIXXZ2XF6TAFM"

def smartapi_login():
    obj = SmartConnect(api_key=API_KEY)
    totp = pyotp.TOTP(TOTP_SECRET).now()

    try:
        session_data = obj.generateSession(CLIENT_ID, PASSWORD, totp)
        feed_token = obj.getfeedToken()
        refresh_token = session_data['data']['refreshToken']

        print("✅ Logged in to SmartAPI")
        return {
            "client": obj,
            "feed_token": feed_token,
            "refresh_token": refresh_token,
            "login_data": session_data
        }

    except Exception as e:
        print("❌ SmartAPI login failed:", e)
        return None

# Example usage
if __name__ == "__main__":
    smartapi_login()
