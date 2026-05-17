# Exploratory Data Analysis (EDA) Project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Create Sample Dataset
data = {
    "Age": [22, 25, 30, 35, 40, 28, 32, 45, 50, 29],
    "Salary": [25000, 30000, 50000, 65000, 80000, 35000, 48000, 90000, 100000, 40000],
    "Experience": [1, 2, 5, 7, 10, 3, 4, 12, 15, 3],
    "PerformanceScore": [60, 65, 75, 80, 90, 70, 72, 95, 98, 68]
}

df = pd.DataFrame(data)
# Step 2: Display Dataset
print("\n First 5 Rows:")
print(df.head()
# Step 3: Dataset Information
print("\n Dataset Information:")
print(df.info())
# Step 4: Statistical Summary
print("\n📊 Statistical Summary:")
print(df.describe())
# Step 5: Missing Values
print("\n Missing Values:")
print(df.isnull().sum())
# Step 6: Correlation Analysis
print("\n  Correlation Matrix:")
print(df.corr())
# Step 7: Data Visualization

sns.set(style="whitegrid")

# 1. Salary Distribution
plt.figure(figsize=(6,4))
sns.histplot(df["Salary"], bins=5, kde=True)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Count")
plt.show()

# 2. Age vs Salary
plt.figure(figsize=(6,4))
sns.scatterplot(x="Age", y="Salary", data=df)
plt.title("Age vs Salary")
plt.show()

# 3. Experience vs Performance
plt.figure(figsize=(6,4))
sns.barplot(x="Experience", y="PerformanceScore", data=df)
plt.title("Experience vs Performance Score")
plt.show()

# 4. Correlation Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(), annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.show()
# Step 8: Insights
print("\n📌 Insights:")
print("- Salary increases with experience")
print("- Performance score improves with experience")
print("- Strong positive correlation between salary and performance")
print("- Data visualization helps identify trends clearly")