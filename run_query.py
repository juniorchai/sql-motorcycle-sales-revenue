"""
run_query.py
------------
Loads sales.csv into an in-memory SQLite database and runs
analyze_motor_sales.sql, printing the result to the terminal.

Usage:
    python run_query.py
"""

import pandas as pd
import sqlite3

# Load CSV into in-memory SQLite
df = pd.read_csv("sales.csv")
df["date"] = pd.to_datetime(df["date"])
con = sqlite3.connect(":memory:")
df.to_sql("sales", con, index=False)

# Run SQL file (SQLite version - uses strftime instead of EXTRACT)
query = """
SELECT
    product_line,
    CASE
        WHEN CAST(strftime('%m', date) AS INT) = 6 THEN 'June'
        WHEN CAST(strftime('%m', date) AS INT) = 7 THEN 'July'
        WHEN CAST(strftime('%m', date) AS INT) = 8 THEN 'August'
    END AS month,
    warehouse,
    ROUND(SUM(total) - SUM(payment_fee), 2) AS net_revenue

FROM sales
WHERE client_type = 'Wholesale'
GROUP BY product_line, month, warehouse
ORDER BY product_line, month, net_revenue DESC
"""

revenue_by_product_line = pd.read_sql_query(query, con)
con.close()

# Display result
print("=" * 65)
print("Motorcycle Parts - Wholesale Net Revenue (Jun-Aug 2021)")
print("=" * 65)
print(revenue_by_product_line.to_string(index=False))
print(f"\n✅ {len(revenue_by_product_line)} rows returned")
print(f"💰 Total net revenue: ${revenue_by_product_line['net_revenue'].sum():,.2f}")
