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
    "NIFTYIT": {
        "exchange": "NSE",
        "tradingsymbol": "NIFTY IT",
    },
    "SENSEX": {
        "exchange": "BSE",
        "tradingsymbol": "SENSEX",
    },
}