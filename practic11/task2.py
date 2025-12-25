import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("comptagevelo2014.csv", parse_dates=["Date"])

print(df.head())
print(df.info())
print(df.describe())

numeric_df = df.drop(columns=["Date"])
total_all = numeric_df.sum().sum()
print(f"Total number per year: {total_all}")

path_totals = numeric_df.sum().sort_values(ascending=False)
print(path_totals)

df["Month"] = df["Date"].dt.month
top_3 = path_totals.index[:3].tolist()

for path in top_3:
    monthly_sum = df.groupby("Month")[path].sum()
    print(f"Track {path}: peak in month N{monthly_sum.idxmax()}")

plt.figure(figsize=(10, 6))
df.groupby("Month")[top_3[0]].sum().plot(kind="bar", color="skyblue")
plt.title(f"Performance {top_3[0]} by month (2014)")
plt.xlabel("Month")
plt.ylabel("Bike number")
plt.show()