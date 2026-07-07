from data.market_data_service import MarketDataService
from data.instrument_manager import InstrumentManager

from indicators.indicator_manager import IndicatorManager
from structure.structure_manager import StructureManager


class TradingApplication:

    def __init__(self):

        self.market = MarketDataService()
        self.instrument = InstrumentManager()
        self.indicator = IndicatorManager()
        self.structure = StructureManager()

    def run(self, config):

        ce = None
        pe = None
        ce_df = None
        pe_df = None
        
        # ---------------------------------------
        # Load Spot Data
        # ---------------------------------------

        df = self.market.get_spot_data(
            symbol=config["symbol"],
            interval=config["interval"],
            trading_date=config["trading_date"],
            lookback_days=config["lookback_days"],
        )

        # ---------------------------------------
        # Load Option Data - ATM
        # ---------------------------------------

        # spot_price = df.iloc[0]["Open"]
        spot_price = df.iloc[-1]["Open"]
        
        ce = self.instrument.get_atm_option(
                config["symbol"],
                spot_price,
                "CE",
            )

        pe = self.instrument.get_atm_option(
                config["symbol"],
                spot_price,
                "PE",
            )

        ce_df = self.market.get_option_data_by_token(
                instrument_token=ce["instrument_token"],
                interval=config["interval"],
                trading_date=config["trading_date"],
                lookback_days=1,
            )

        pe_df = self.market.get_option_data_by_token(
                instrument_token=pe["instrument_token"],
                interval=config["interval"],
                trading_date=config["trading_date"],
                lookback_days=1,
            )
        
        print(ce_df.columns)
        
        ce_df["VWAP"] = (
                (ce_df["Close"] * ce_df["Volume"]).cumsum()
                / ce_df["Volume"].cumsum()
            )

        pe_df["VWAP"] = (
                (pe_df["Close"] * pe_df["Volume"]).cumsum()
                / pe_df["Volume"].cumsum()
            )

        df["CE_Volume"] = ce_df["Volume"]
        df["PE_Volume"] = pe_df["Volume"]

        df["CE_OI"] = ce_df["OI"]
        df["PE_OI"] = pe_df["OI"]

        df["CE_Close"] = ce_df["Close"]
        df["PE_Close"] = pe_df["Close"]

        df["CE_VWAP"] = ce_df["VWAP"]
        df["PE_VWAP"] = pe_df["VWAP"]

        # ---------------------------------------
        # Indicators
        # ---------------------------------------

        df = self.indicator.calculate(
            df,
            config["settings"],
        )

        # ---------------------------------------
        # Market Structure
        # ---------------------------------------

        df = self.structure.calculate(df)

        # ---------------------------------------
        # Keep Selected Trading Day
        # ---------------------------------------

        df = df[df.index.date == config["trading_date"]]
        
        if df.empty:
            return None

        if ce_df is not None:
            ce_df["Volume_SMA20"] = (
                ce_df["Volume"]
                .rolling(20)
                .mean()
            )

        if pe_df is not None:
            pe_df["Volume_SMA20"] = (
                pe_df["Volume"]
                .rolling(window=20, min_periods=1)
            .mean()
        )

        return {
           "data": df,
            "ce": ce,
            "pe": pe,
            "ce_df": ce_df,
            "pe_df": pe_df,
        }
    

