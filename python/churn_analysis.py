import pandas as pd

# Load the customer churn dataset
file_path = "data/raw/Telco-Customer-Churn.csv"
df = pd.read_csv(file_path)

# 1. Dataset size
print("\n--- CUSTOMER CHURN DATASET ---")
print("Rows and columns:", df.shape)

# 2. Preview records
print("\n--- FIRST 5 CUSTOMERS ---")
print(df.head())

# 3. Column names
print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

# 4. Dataset information
print("\n--- DATA TYPES ---")
df.info()

# 5. Missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# 6. Churn distribution
print("\n--- CHURN DISTRIBUTION ---")
print(df["Churn"].value_counts())

# 7. Churn percentage
print("\n--- CHURN PERCENTAGE ---")
print(
    df["Churn"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)
# 8. Check duplicate records
print("\n--- DUPLICATE RECORDS ---")
print("Duplicate rows:", df.duplicated().sum())

# 9. Check customer ID uniqueness
print("\n--- CUSTOMER ID CHECK ---")
print("Unique customer IDs:", df["customerID"].nunique())

# 10. Check TotalCharges data type
print("\n--- TOTAL CHARGES DATA TYPE ---")
print(df["TotalCharges"].dtype)

# 11. Find blank TotalCharges values
print("\n--- BLANK TOTAL CHARGES ---")
print("Blank TotalCharges:", df["TotalCharges"].astype(str).str.strip().eq("").sum())

# 12. Clean TotalCharges
print("\n--- CLEANING TOTAL CHARGES ---")

# Convert blank strings to missing values, then convert to numbers
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"].str.strip(),
    errors="coerce"
)

print("Missing TotalCharges after conversion:",
      df["TotalCharges"].isnull().sum())

# Investigate records with missing TotalCharges
print("\n--- CUSTOMERS WITH MISSING TOTAL CHARGES ---")
print(
    df.loc[
        df["TotalCharges"].isnull(),
        ["customerID", "tenure", "MonthlyCharges", "TotalCharges"]
    ]
)

# Remove rows with missing TotalCharges
df_clean = df.dropna(subset=["TotalCharges"]).copy()

print("\n--- CLEANED DATASET ---")
print("Rows before cleaning:", len(df))
print("Rows after cleaning:", len(df_clean))
print("Missing TotalCharges after cleaning:",
      df_clean["TotalCharges"].isnull().sum())

# 13. Save the cleaned dataset
from pathlib import Path

output_path = Path(__file__).resolve().parent.parent / "data" / "processed" / "customer_churn_cleaned.csv"
output_path.parent.mkdir(parents=True, exist_ok=True)

df_clean.to_csv(output_path, index=False)

print("\n--- EXPORT CLEANED DATASET ---")
print("Cleaned dataset saved to:", output_path)
print("Final dataset shape:", df_clean.shape)

# 14. Business analysis: churn by contract type
print("\n--- CHURN RATE BY CONTRACT TYPE ---")

contract_churn = (
    df_clean.groupby("Contract")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .round(2)
    .sort_values(ascending=False)
)

print(contract_churn)

# 15. Business analysis: churn by customer tenure
print("\n--- CHURN RATE BY TENURE GROUP ---")

df_clean["TenureGroup"] = pd.cut(
    df_clean["tenure"],
    bins=[-1, 12, 24, 48, 72],
    labels=["0-12 months", "13-24 months", "25-48 months", "49-72 months"]
)

tenure_churn = (
    df_clean.groupby("TenureGroup", observed=False)["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .round(2)
)

print(tenure_churn)

# 16. Business analysis: monthly charges
print("\n--- MONTHLY CHARGES BY CHURN STATUS ---")

charges_analysis = (
    df_clean.groupby("Churn")["MonthlyCharges"]
    .agg(["mean", "median"])
    .round(2)
)

print(charges_analysis)

# 17. Business analysis: churn by payment method
print("\n--- CHURN RATE BY PAYMENT METHOD ---")

payment_churn = (
    df_clean.groupby("PaymentMethod")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .round(2)
    .sort_values(ascending=False)
)

print(payment_churn)

# 18. Visualizations

import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Create a folder for charts
Path("reports").mkdir(exist_ok=True)

sns.set_theme(style="whitegrid")

# Chart 1: Churn rate by contract type
plt.figure(figsize=(9, 5))
sns.barplot(
    x=contract_churn.index,
    y=contract_churn.values
)
plt.title("Customer Churn Rate by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")
plt.tight_layout()
plt.savefig("reports/churn_by_contract.png", dpi=300)
plt.close()

# Chart 2: Churn rate by tenure group
plt.figure(figsize=(9, 5))
sns.barplot(
    x=tenure_churn.index.astype(str),
    y=tenure_churn.values
)
plt.title("Customer Churn Rate by Tenure")
plt.xlabel("Customer Tenure")
plt.ylabel("Churn Rate (%)")
plt.tight_layout()
plt.savefig("reports/churn_by_tenure.png", dpi=300)
plt.close()

# Chart 3: Average monthly charges by churn status
plt.figure(figsize=(7, 5))
sns.barplot(
    data=df_clean,
    x="Churn",
    y="MonthlyCharges",
    estimator="mean",
    errorbar=None
)
plt.title("Average Monthly Charges by Churn Status")
plt.xlabel("Customer Churn")
plt.ylabel("Average Monthly Charges")
plt.tight_layout()
plt.savefig("reports/monthly_charges_by_churn.png", dpi=300)
plt.close()

# Chart 4: Churn rate by payment method
plt.figure(figsize=(10, 5))
sns.barplot(
    x=payment_churn.values,
    y=payment_churn.index
)
plt.title("Customer Churn Rate by Payment Method")
plt.xlabel("Churn Rate (%)")
plt.ylabel("Payment Method")
plt.tight_layout()
plt.savefig("reports/churn_by_payment_method.png", dpi=300)
plt.close()

print("\n--- CHARTS CREATED ---")
print("Check the reports folder for four PNG charts.")

