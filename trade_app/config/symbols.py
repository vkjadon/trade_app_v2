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
    "SENSEX": {
        "exchange": "BSE",
        "tradingsymbol": "SENSEX",
    },
    "RELIANCE": {
        "exchange": "NSE",
        "tradingsymbol": "RELIANCE",
    },
    "HDFC": {
        "exchange": "NSE",
        "tradingsymbol": "HDFCBANK",
    },
}

OPTION_INDICES = {
    "NIFTY": {
        "name": "NIFTY",
        "segment": "NFO-OPT",
        "step": 50,
    },
    "BANKNIFTY": {
        "name": "BANKNIFTY",
        "segment": "NFO-OPT",
        "step": 100,
    },
    "SENSEX": {
        "name": "SENSEX",
        "segment": "BFO-OPT",
        "step": 100,
    },
    "RELIANCE": {
        "name": "RELIANCE",
        "segment": "NFO-OPT",
        "step": 10,
    },
    "HDFC": {
        "name": "HDFCBANK",
        "segment": "NFO-OPT",
        "step": 10,
    },
}