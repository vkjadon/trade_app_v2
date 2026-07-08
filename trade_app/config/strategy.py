"""
=========================================================
Trade App V2 - Strategy Configuration
=========================================================
Modify strategy behaviour from this file.
No changes should be required in the rule engine.
"""

# =========================================================
# SIGNAL ENGINE
# =========================================================

BUY_THRESHOLD = 85
WATCH_THRESHOLD = 70

# =========================================================
# RULE ENABLE / DISABLE
# =========================================================

USE_TIME_FILTER = True
USE_EMA = True
USE_EMA_SLOPE = True
USE_RSI = True
USE_MACD = True
USE_CANDLE = True
USE_BREAKOUT = True
USE_VOLUME = False
USE_ATR = False
USE_VWAP = False
USE_OI = False
USE_PCR = False
USE_GREEKS = False

# =========================================================
# RULE WEIGHTS
# =========================================================



EMA_SCORE = 20
EMA_SLOPE_SCORE = 10

RSI_SCORE = 15
RSI_SLOPE_SCORE = 5

MACD_SCORE = 20
MACD_HISTOGRAM_SCORE = 5

CANDLE_SCORE = 15
BREAKOUT_SCORE = 15
TIME_SCORE = 5
VOLUME_SCORE = 5
ATR_SCORE = 5
VWAP_SCORE = 10
OI_SCORE = 10
PCR_SCORE = 10
GREEKS_SCORE = 10

MACD_MOMENTUM_SCORE = 5

RSI_SLOPE_SCORE = 5

EMA_SLOPE_SCORE = 10


# =========================================================
# RSI
# =========================================================

RSI_BULL = 60
RSI_BEAR = 40

# =========================================================
# EMA
# =========================================================

EMA_PERIOD = 20

# =========================================================
# MACD
# =========================================================

MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9

# =========================================================
# CANDLE QUALITY
# =========================================================

MIN_BODY_PERCENT = 0.50

# Candle must close within this % of High (BUY)
BULL_CLOSE_PERCENT = 0.80

# Candle must close within this % of Low (SELL)
BEAR_CLOSE_PERCENT = 0.20

# =========================================================
# BREAKOUT
# =========================================================

USE_PREVIOUS_HIGH_LOW = True

# =========================================================
# TIME FILTER
# =========================================================

IGNORE_FIRST_CANDLES = 3

IGNORE_OPENING_RANGE = True
OPENING_RANGE_MINUTES = 15

LAST_ENTRY_HOUR = 15
LAST_ENTRY_MINUTE = 0

# =========================================================
# ATR
# =========================================================

ATR_PERIOD = 14

ATR_MULTIPLIER = 1.20

# =========================================================
# RELATIVE VOLUME
# =========================================================

RELATIVE_VOLUME_THRESHOLD = 1.20

# =========================================================
# VWAP
# =========================================================

VWAP_DISTANCE_PERCENT = 0.15

BREAKOUT_SCORE = 15

BUY_THRESHOLD = 80
REVERSAL_MARGIN = 20
COOLDOWN_CANDLES = 2
MIN_CONFIDENCE = "HIGH"

RSI_MOMENTUM_SCORE = 5


