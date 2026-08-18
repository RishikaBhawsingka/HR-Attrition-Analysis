import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../raw/HR-Employee-Attrition.csv")

print("\n===== SHAPE =====")
print(df.shape)

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== COLUMNS =====")
print(df.columns.tolist())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATES =====")
print(df.duplicated().sum())

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe().T)

print("\n===== CATEGORICAL COLUMNS =====")

categorical_cols = df.select_dtypes(include="object").columns

for col in categorical_cols:
    print(f"\n--- {col} ---")
    print(df[col].value_counts())

print("\n===== NUMERICAL COLUMNS =====")
print(df.select_dtypes(include=np.number).columns.tolist())

# Attrition distribution
if "Attrition" in df.columns:
    print("\n===== ATTRITION =====")
    print(df["Attrition"].value_counts())

    print("\n===== ATTRITION % =====")
    print(df["Attrition"].value_counts(normalize=True) * 100)

# =========================
# BUSINESS EDA
# =========================

print("\n===== ATTRITION BY DEPARTMENT =====")
print(pd.crosstab(
    df["Department"],
    df["Attrition"],
    normalize="index"
).round(3) * 100)


print("\n===== ATTRITION BY JOB ROLE =====")
print(pd.crosstab(
    df["JobRole"],
    df["Attrition"],
    normalize="index"
).round(3) * 100)


print("\n===== ATTRITION BY OVERTIME =====")
print(pd.crosstab(
    df["OverTime"],
    df["Attrition"],
    normalize="index"
).round(3) * 100)


print("\n===== ATTRITION BY JOB SATISFACTION =====")
print(pd.crosstab(
    df["JobSatisfaction"],
    df["Attrition"],
    normalize="index"
).round(3) * 100)


print("\n===== ATTRITION BY JOB LEVEL =====")
print(pd.crosstab(
    df["JobLevel"],
    df["Attrition"],
    normalize="index"
).round(3) * 100)


print("\n===== ATTRITION BY BUSINESS TRAVEL =====")
print(pd.crosstab(
    df["BusinessTravel"],
    df["Attrition"],
    normalize="index"
).round(3) * 100)


print("\n===== ATTRITION BY WORK-LIFE BALANCE =====")
print(pd.crosstab(
    df["WorkLifeBalance"],
    df["Attrition"],
    normalize="index"
).round(3) * 100)


print("\n===== ATTRITION BY AGE GROUP =====")

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[17, 25, 35, 45, 55, 65],
    labels=["18-25", "26-35", "36-45", "46-55", "56-65"]
)

print(pd.crosstab(
    df["AgeGroup"],
    df["Attrition"],
    normalize="index"
).round(3) * 100)