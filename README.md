# Trade App V2

Professional Intraday Trading Platform using Zerodha Kite API

---

# Features

- Historical Market Data
- Interactive Candlestick Charts
- EMA
- RSI
- MACD
- ATR
- VWAP
- Relative Volume
- Strategy Engine
- Trade Engine
- Trade Book
- Signal Generation
- Streamlit UI

---

# Technology Stack

Python 3.13
UV Package Manager
Streamlit
Plotly
Pandas
NumPy
Kite Connect API

---

# Project Structure

trade_app_v2/

    app.py

    core/
        application.py

    config/
        ...

    data/
        market_data.py
        market_data_service.py
        instrument_manager.py
        kite_client.py

    indicators/
        ema.py
        rsi.py
        macd.py
        atr.py
        vwap.py
        volume.py
        indicator_manager.py

    strategy/
        strategy_manager.py
        rule_engine.py
        breakout_rule.py
        candle_rule.py
        ema_rule.py
        macd_rule.py
        rsi_rule.py
        time_rule.py

    engine/
        trade_engine.py

    charts/
        candlestick.py
        rsi_chart.py
        macd_chart.py
        charts_panel.py

    widgets/
        sidebar.py
        market_widget.py
        indicator_widget.py
        trade_book.py

    models/
        trade.py

---

# Daily Startup

## Step 1

Activate Environment

uv sync

or

source .venv/bin/activate

---

## Step 2

Generate Zerodha Access Token

uv run python auth/login.py

Complete login in browser.

The access token is stored.

---

## Step 3

Start Streamlit

uv run streamlit run app.py

---

# Application Flow

Sidebar

↓

Market Data

↓

Indicator Manager

↓

Strategy Engine

↓

Trade Engine

↓

Charts

↓

Trade Book

---

# Indicators Used

EMA20

Purpose

Trend Detection

---

RSI 14

Purpose

Momentum Confirmation

---

MACD

Purpose

Momentum + Trend Confirmation

---

ATR

Purpose

Future Stop Loss and Volatility Filter

---

VWAP

Purpose

Institutional Direction

(Currently Optional)

---

Relative Volume

Purpose

Participation Confirmation

(Currently Optional)

---

# Signal Generation

Signals are generated using a weighted scoring model.

Current Rules

EMA

Price above EMA

EMA Rising

RSI

RSI > 55

RSI Rising

MACD

MACD > Signal

Histogram Increasing

Price Action

Strong Bull Candle

Strong Bear Candle

Breakout

Previous Candle High Break

Previous Candle Low Break

Time

Ignore Opening Noise

---

# Confidence

Signals are classified as

Low

Medium

High

based on accumulated score.

---

# Trade Engine

Current Entry

BUY CE

BUY PE

Current Exit

Opposite Signal

End Of Day

Future Versions

Stop Loss

Target

Trailing Stop

Risk Management

---

# Trade Book

Displays

Entry Time

Exit Time

Entry Price

Exit Price

Points

Running P/L

Score

Confidence

Reasons

---

# Current Version

Version 2.0

Implemented

✔ Historical Data

✔ Charts

✔ Indicators

✔ Strategy Engine

✔ Trade Engine

✔ Trade Book

✔ Date Picker

✔ Lookback Days

✔ Sidebar Widgets

---

# Planned

Market Structure

Opening Range Breakout

Support Resistance

ADX

Relative Volume

Option Chain

OI

PCR

Greeks

Backtesting

Paper Trading

Live Trading

---

# Coding Guidelines

One Responsibility Per Class

Business Logic outside Streamlit

Reusable Components

Keep app.py lightweight

Return Models instead of Dictionaries (future)

---

# Future Roadmap

Phase 1

Market Structure

Phase 2

Trend Filters

Phase 3

Options Intelligence

Phase 4

Backtesting

Phase 5

Paper Trading

Phase 6

Live Trading
