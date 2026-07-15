from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent

csv_file = (
    BASE_DIR
    / "data"
    / "raw"
    / "NIFTY"
    / "2026"
    / "07.csv"
)

df = pd.read_csv(csv_file)

print(df.columns.tolist())

print()

print(df.head())

print(df["Datetime"].iloc[0])
print(type(df["Datetime"].iloc[0]))