import pandas as pd
import mysql.connector
from pathlib import Path
from getpass import getpass

# Find the project folder and cleaned CSV
project_dir = Path(__file__).resolve().parent.parent
csv_path = project_dir / "data" / "processed" / "customer_churn_cleaned.csv"

# Load the cleaned dataset
df = pd.read_csv(csv_path)
print(f"CSV loaded: {len(df)} rows")

# Connect to MySQL
password = getpass("Enter your MySQL root password: ")

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password=password,
    database="customer_churn_db"
)

cursor = conn.cursor()

try:
    # Check whether the table already contains data
    cursor.execute("SELECT COUNT(*) FROM customer_churn")
    existing_rows = cursor.fetchone()[0]

    if existing_rows > 0:
        print(f"The table already contains {existing_rows} rows.")
        print("Import cancelled to prevent duplicate records.")

    else:
        columns = list(df.columns)
        column_names = ", ".join(f"`{col}`" for col in columns)
        placeholders = ", ".join(["%s"] * len(columns))

        sql = f"""
            INSERT INTO customer_churn ({column_names})
            VALUES ({placeholders})
        """

        records = [
            tuple(None if pd.isna(value) else value for value in row)
            for row in df.itertuples(index=False, name=None)
        ]

        cursor.executemany(sql, records)
        conn.commit()

        print(f"Successfully imported {cursor.rowcount} records.")

    cursor.execute("SELECT COUNT(*) FROM customer_churn")
    print("Total rows in MySQL:", cursor.fetchone()[0])

except Exception as error:
    conn.rollback()
    print("Import failed:", error)

finally:
    cursor.close()
    conn.close()
