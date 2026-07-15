from datetime import date
from pathlib import Path
from datetime import time

ROOT = Path(__file__).resolve().parents[1]

INSTRUMENTS = [
    "SENSEX",
    "NIFTY",
    "BANKNIFTY",
]

ROOT = Path(__file__).resolve().parents[0]

INSTRUMENT_FILE = ROOT / "data" / "instruments" / "instruments.csv"

INTERVAL = "5minute"

CANDLE_INTERVAL = 5
CANDLES_PER_DAY = 75

MARKET_OPEN = time(9, 15)
MARKET_CLOSE = time(15, 25)

START_YEAR = 2021
END_YEAR = 2026

START_DATE = date(2021, 1, 1)

RAW_DATA_PATH = "ai/data/raw"
FEATURE_PATH = "ai/data/features"
MODEL_PATH = "ai/data/models"

SPOT_INDICES = {
    "SENSEX": {
        "exchange": "BSE",
        "tradingsymbol": "SENSEX",
    },
    "NIFTY": {
        "exchange": "NSE",
        "tradingsymbol": "NIFTY 50",
    },
    "BANKNIFTY": {
        "exchange": "NSE",
        "tradingsymbol": "NIFTY BANK",
    },  
}