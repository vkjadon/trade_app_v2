from pathlib import Path

import pandas as pd


class DatasetManager:

    def __init__(self):

        self.root = (
            Path(__file__).resolve().parents[1]
            / "data"
            / "raw"
        )

    def summary(self):

        instruments = 0
        years = set()
        months = 0
        files = 0
        candles = 0
        size = 0

        records = []

        if not self.root.exists():

            return {
                "summary": {
                    "instruments": 0,
                    "years": 0,
                    "months": 0,
                    "files": 0,
                    "candles": 0,
                    "size_mb": 0,
                },
                "records": [],
            }

        for symbol_dir in sorted(self.root.iterdir()):

            if not symbol_dir.is_dir():
                continue

            instruments += 1

            for year_dir in sorted(symbol_dir.iterdir()):

                if not year_dir.is_dir():
                    continue

                years.add(year_dir.name)

                for csv in sorted(year_dir.glob("*.csv")):

                    files += 1
                    months += 1

                    df = pd.read_csv(csv)

                    candle_count = len(df)

                    candles += candle_count

                    file_size = csv.stat().st_size

                    size += file_size

                    records.append(
                        {
                            "Instrument": symbol_dir.name,
                            "Year": int(year_dir.name),
                            "Month": csv.stem,
                            "Candles": candle_count,
                            "Size (KB)": round(file_size / 1024, 1),
                        }
                    )

        return {

            "summary": {

                "instruments": instruments,

                "years": len(years),

                "months": months,

                "files": files,

                "candles": candles,

                "size_mb": round(size / 1024 / 1024, 2),

            },

            "records": records,

        }