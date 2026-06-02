import pandas as pd
import os

DATA_DIR = "data/raw"

csv_files = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]

print(f"Found {len(csv_files)} CSV files\n")

for file in csv_files:

    path = os.path.join(DATA_DIR, file)

    print("=" * 60)
    print("FILE:", file)

    df = pd.read_csv(path)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nHead:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\n")