# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

# Display First 5 Rows
print("First 5 Rows:")
print(df.head())

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove Missing Values
df = df.dropna()

# Rename Columns (optional)
df.columns = df.columns.str.strip()

# Dataset Information
print("\nDataset Info:")
print(df.info())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Convert Date Column
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# -----------------------------
# Unemployment Trend Analysis
# -----------------------------

plt.figure(figsize=(12,6))
sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', data=df)

plt.title("Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("unemployment_trend.png")
plt.show()

# -----------------------------
# Covid-19 Impact Analysis
# -----------------------------

covid_period = df[df['Date'] >= '2020-03-01']

plt.figure(figsize=(12,6))
sns.lineplot(
    x='Date',
    y='Estimated Unemployment Rate (%)',
    data=covid_period,
    color='red'
)

plt.title("Unemployment During Covid-19")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# -----------------------------
# State-wise Analysis
# -----------------------------

state_avg = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean()

print("\nAverage Unemployment Rate by State:")
print(state_avg.sort_values(ascending=False))

# Top 10 States
top_states = state_avg.sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
top_states.plot(kind='bar')

plt.title("Top 10 States with Highest Unemployment")
plt.xlabel("State")
plt.ylabel("Average Unemployment Rate (%)")
plt.tight_layout()

plt.show()
