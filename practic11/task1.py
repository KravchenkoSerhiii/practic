import pandas as pd

institutions = {
    "Гімназія N1": {"type": "школа", "students": 500, "avg_score": 175.5},
    "Ліцей N2": {"type": "школа", "students": 450, "avg_score": 182.0},
    "Політехнікум": {"type": "технікум", "students": 800, "avg_score": 160.2},
    "ВПУ N6": {"type": "училище", "students": 300, "avg_score": 155.0},
    "ЗОШ N10": {"type": "школа", "students": 620, "avg_score": 168.4},
    "Коледж СНАУ": {"type": "технікум", "students": 550, "avg_score": 170.1}
}

print("Entry dict:", institutions)

df = pd.DataFrame.from_dict(institutions, orient="index")
df.index.name = "name"
df = df.reset_index()

print("\n1. First 3 rows:")
print(df.head(3))

print("\n2. Data types:")
print(df.dtypes)

print("\n3. Numbers of rows and columns:")
print(df.shape)

print("\n4. Statistics:")
print(df.describe())

df["budget_uah"] = df["students"] * 1000

print("\n5. Filtration (Number of students more than 500):")
print(df[df["students"] > 500])

print("\n6. Sorting students from top to down")
print(df.sort_values(by="students", ascending=False))

print("\n7. AVG by type")
print(df.groupby("type")[["students", "avg_score"]].mean())


print("\n8. Max number of students by category:")
print(df.groupby("type")["students"].max())

print("\n9. Number of unique types:", df["type"].nunique())
