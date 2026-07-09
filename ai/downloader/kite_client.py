from kiteconnect import KiteConnect
from dotenv import load_dotenv
import os

load_dotenv()

KITE_API_KEY = os.getenv("KITE_API_KEY")
KITE_API_SECRET = os.getenv("KITE_API_SECRET")
KITE_ACCESS_TOKEN = os.getenv("KITE_ACCESS_TOKEN")

_kite = None

def get_kite():

    global _kite
    if _kite is None:
        kite = KiteConnect(api_key=KITE_API_KEY)
        kite.set_access_token(KITE_ACCESS_TOKEN)
        _kite = kite

    return _kite