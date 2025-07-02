# backend/fetch/smartapi_login.py

from SmartApi.smartConnect import SmartConnect
import pyotp
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
CLIENT_ID = os.getenv("CLIENT_ID")
PASSWORD = os.getenv("PASSWORD")
TOTP_SECRET = os.getenv("TOTP_SECRET")

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
