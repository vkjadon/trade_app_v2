from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

INSTRUMENTS = [
    "NIFTY",
    "BANKNIFTY",
    "SENSEX",
]

ROOT = Path(__file__).resolve().parents[0]

INSTRUMENT_FILE = ROOT / "data" / "instruments" / "instruments.csv"

INTERVAL = "5minute"

START_YEAR = 2021
END_YEAR = 2026

START_DATE = date(2021, 1, 1)

RAW_DATA_PATH = "ai/data/raw"
FEATURE_PATH = "ai/data/features"
MODEL_PATH = "ai/data/models"

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
}