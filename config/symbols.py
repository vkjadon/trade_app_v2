"""
Spot Indices supported by the application.

The instrument token is resolved dynamically from the
instrument master.
"""

SPOT_INDICES = {
    "NIFTY": {
        "exchange": "NSE",
        "tradingsymbol": "NIFTY 50",
    },
    "BANKNIFTY": {
        "exchange": "NSE",
        "tradingsymbol": "NIFTY BANK",
    },
    "FINNIFTY": {
        "exchange": "NSE",
        "tradingsymbol": "NIFTY FIN SERVICE",
    },
    "MIDCPNIFTY": {
        "exchange": "NSE",
        "tradingsymbol": "NIFTY MID SELECT",
    },
    "SENSEX": {
        "exchange": "BSE",
        "tradingsymbol": "SENSEX",
    },
}