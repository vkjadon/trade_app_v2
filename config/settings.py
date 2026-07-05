"""
Application Settings
Loads environment variables from .env
"""

from dotenv import load_dotenv
import os

load_dotenv()


# -------------------------------------------------------
# Kite Credentials
# -------------------------------------------------------

KITE_API_KEY = os.getenv("KITE_API_KEY")

KITE_API_SECRET = os.getenv("KITE_API_SECRET")

KITE_ACCESS_TOKEN = os.getenv("KITE_ACCESS_TOKEN")


# -------------------------------------------------------
# Market Defaults
# -------------------------------------------------------

DEFAULT_INDEX = "NIFTY"

DEFAULT_INTERVAL = "5minute"

DEFAULT_HISTORY_DAYS = 5


# -------------------------------------------------------
# Cache
# -------------------------------------------------------

CACHE_FOLDER = "cache"

INSTRUMENT_FILE = "cache/instruments.csv"