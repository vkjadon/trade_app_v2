from datetime import date

from config import (
    INSTRUMENTS,
    INTERVAL,
    START_YEAR,
    END_YEAR,
)


class DownloadManager:

    def __init__(
        self,
        downloader,
        validator,
        writer,
        instrument,
    ):
        self.downloader = downloader
        self.validator = validator
        self.writer = writer
        self.instrument = instrument

    def run(
        self,
        symbols,
        interval,
        start_date,
        end_date,
        download_master=False,
    ):

        for symbol in symbols:

            self._download_instrument(
                symbol,
                interval,
                start_date,
                end_date,
                download_master,
            )


    def _download_instrument(
        self,
        symbol,
        interval,
        start_date,
        end_date,
        download_master,
    ):

        if download_master:
            self.instrument.refresh()
        
        token = self.instrument.get_spot_token(symbol)

        today = date.today()

        for year in range(
            START_YEAR,
            END_YEAR + 1,
        ):

            last_month = 12

            if year == today.year:
                last_month = today.month

            for month in range(
                1,
                last_month + 1,
            ):

                self._download_month(
                    token,
                    symbol,
                    year,
                    month,
                )

    def _download_month(
        self,
        token,
        symbol,
        year,
        month,
    ):

        if self.writer.exists(
            symbol,
            year,
            month,
        ):
            print(f"Skipping : {symbol} {year}-{month:02d}")
            return

        df = self.downloader.download_month(
            instrument_token=token,
            interval=INTERVAL,
            year=year,
            month=month,
        )

        if df.empty:
            print(f"No Data : {symbol} {year}-{month:02d}")
            return

        if not self.validator.validate(df):
            print(f"Validation Failed : {symbol} {year}-{month:02d}")
            return

        self.writer.save(
            symbol=symbol,
            year=year,
            month=month,
            df=df,
        )