"""
Singleton Kite Client
"""

from kiteconnect import KiteConnect

from config.settings import (
    KITE_API_KEY,
    KITE_ACCESS_TOKEN,
)

_kite = None


def get_kite():

    global _kite

    if _kite is None:

        kite = KiteConnect(
            api_key=KITE_API_KEY
        )

        kite.set_access_token(
            KITE_ACCESS_TOKEN
        )

        _kite = kite

    return _kite