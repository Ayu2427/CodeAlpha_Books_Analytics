from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
df = pd.read_csv(BASE / "data" / "books_clean.csv")

print("Shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicates:", df.duplicated().sum())
print("\nDescriptive statistics:\n", df[["Price_GBP","Rating_Num","Title_Length","Word_Count"]].describe())

corr = df["Price_GBP"].corr(df["Rating_Num"])
q1, q3 = df["Price_GBP"].quantile([0.25, 0.75])
iqr = q3 - q1
outliers = df[(df["Price_GBP"] < q1 - 1.5*iqr) | (df["Price_GBP"] > q3 + 1.5*iqr)]

print(f"\nAverage price: £{df.Price_GBP.mean():.2f}")
print(f"Median price: £{df.Price_GBP.median():.2f}")
print(f"Average rating: {df.Rating_Num.mean():.2f}/5")
print(f"In-stock rate: {df.Availability.eq('In Stock').mean()*100:.1f}%")
print(f"Price-rating correlation: {corr:.3f}")
print(f"IQR price outliers: {len(outliers)}")
