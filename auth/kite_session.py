import os

from dotenv import load_dotenv
from kiteconnect import KiteConnect

load_dotenv()

_kite = None


def get_kite():

    global _kite

    if _kite is None:

        api_key = os.getenv("KITE_API_KEY")
        access_token = os.getenv("KITE_ACCESS_TOKEN")

        if not api_key:
            raise RuntimeError("KITE_API_KEY missing")

        if not access_token:
            raise RuntimeError(
                "KITE_ACCESS_TOKEN missing. Run auth/login.py first."
            )

        _kite = KiteConnect(api_key=api_key)
        _kite.set_access_token(access_token)

    return _kite