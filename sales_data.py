import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Load Dataset

print("Current Working Directory:")
print(os.getcwd())

# Give full CSV path here
df = pd.read_csv("sales_data.csv")

print("\n✅ First 5 Rows:")
print(df.head())

# Step 2: Basic Information
print("\n📌 Dataset Info:")
print(df.info())

print("\n📊 Statistical Summary:")
print(df.describe())
# Step 3: Data Cleaning

# Missing Values
print("\n❌ Missing Values:")
print(df.isnull().sum())

# Fill numeric columns with mean
for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].mean())

# Fill categorical columns with mode
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\n✅ Missing values handled.")

# Remove Duplicates
df = df.drop_duplicates()
print("\n✅ Duplicates removed.")

# Handle Outliers
for col in df.select_dtypes(include=np.number).columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    df = df[(df[col] >= Q1 - 1.5 * IQR) &
            (df[col] <= Q3 + 1.5 * IQR)]

print("\n✅ Outliers handled.")

# Convert Date Column
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])


# Step 4: Data Visualization

sns.set(style="whitegrid")

# Sales Distribution
if 'Sales' in df.columns:
    plt.figure()
    sns.histplot(df['Sales'], bins=20)
    plt.title("Sales Distribution")
    plt.show()

# Sales by Region
if 'Region' in df.columns and 'Sales' in df.columns:
    plt.figure()
    sns.barplot(x='Region', y='Sales', data=df)
    plt.title("Sales by Region")
    plt.show()

# Time Series Trend
if 'Date' in df.columns and 'Sales' in df.columns:
    df.groupby('Date')['Sales'].sum().plot()
    plt.title("Sales Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.show()

# Correlation Heatmap
plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Matrix")
plt.show()

# Step 5: Save Cleaned Data
df.to_csv("cleaned_sales_data.csv", index=False)

print("\n Cleaned data saved as cleaned_sales_data.csv")
# Step 6: Insights
print("\n📌 Sample Insights:")
print("- Data cleaned successfully")
print("- Outliers removed for better accuracy")
print("- Visualizations generated")