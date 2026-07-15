from pathlib import Path

from dataset.dataset_builder import DatasetBuilder


BASE_DIR = Path(__file__).resolve().parent

csv_file = (
    BASE_DIR
    / "data"
    / "raw"
    / "NIFTY"
    / "2026"
    / "07.csv"
)

builder = DatasetBuilder()

days = builder.prepare(csv_file)

builder.validate(days)

# -------------------------------------------------------
# Inspect incomplete / abnormal days
# -------------------------------------------------------

for trading_day, day_df in days.items():

    if len(day_df) != 75:

        print("\n" + "=" * 70)

        print(f"Trading Day : {trading_day}")

        print(f"Candles     : {len(day_df)}")

        print(
            f"Duplicate Timestamps : "
            f"{day_df['Datetime'].duplicated().sum()}"
        )

        print()

        print(
            "Time Range :",
            day_df["Datetime"].min(),
            "->",
            day_df["Datetime"].max(),
        )

        print()

        print("First 10 Candles")

        print(
            day_df[
                ["Datetime", "Open", "High", "Low", "Close"]
            ].head(10)
        )

        print()

        print("Last 10 Candles")

        print(
            day_df[
                ["Datetime", "Open", "High", "Low", "Close"]
            ].tail(10)
        )

        print()

        if day_df["Datetime"].duplicated().sum() > 0:

            print("Duplicate Rows")

            duplicates = day_df[
                day_df["Datetime"].duplicated(keep=False)
            ]

            print(
                duplicates[
                    ["Datetime", "Open", "High", "Low", "Close"]
                ]
            )

        print("=" * 70)