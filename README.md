# 🏍️ Motorcycle Parts Wholesale Revenue Analysis

![SQL](https://img.shields.io/badge/SQL-PostgreSQL-336791?logo=postgresql) ![Python](https://img.shields.io/badge/Python-3.8-blue?logo=python) ![Pandas](https://img.shields.io/badge/Pandas-Analysis-150458?logo=pandas) ![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

## Overview
SQL + Python analysis of **1,000 motorcycle parts sales orders** across three warehouses to calculate wholesale net revenue by product line, month, and warehouse for **June–August 2021**.  
The goal is to help the board of directors understand revenue performance and identify top-performing product lines and locations.

*Data source: Motorcycle parts company database — modified version via DataCamp*

## Research Questions
| # | Question |
|---|----------|
| 1 | Which product line generates the highest wholesale net revenue? |
| 2 | How does wholesale revenue vary month-to-month? |
| 3 | Which warehouse contributes the most revenue? |
| 4 | What is the net revenue breakdown for each product line × month × warehouse? |

## Key Findings
- 💰 **Total wholesale net revenue: $159,640.08** across Jun–Aug 2021
- 🏆 **Frame & body** is the top product line — **$39,477.51** total net revenue
- 📅 **August** is the strongest month — **$61,455.55** (vs ~$49K in June/July)
- 🏭 **Central warehouse** leads all locations — **$78,855.67** net revenue
- ⚡ **Engine** had the single highest monthly result — **$9,528.71** (Central, August)
- 📉 **Miscellaneous** is the lowest-performing product line — **$15,747.51**

## SQL Techniques Used
- `WHERE` — filter Wholesale orders only
- `CASE WHEN` — convert month number to June / July / August
- `SUM()`, `ROUND()` — calculate and format net revenue
- `GROUP BY` — aggregate by product line, month, warehouse
- `ORDER BY` — sort by product line, month, net revenue descending

## Tools & Libraries
- **SQL (PostgreSQL / SQLite)** · **Python 3.8** · **Pandas**

## Dataset
`sales.csv` — 1,000 rows × 11 columns of motorcycle parts sales orders (June–August 2021).  
Key columns: `client_type`, `product_line`, `date`, `warehouse`, `total`, `payment_fee`

## How to Run
```bash
git clone https://github.com/JuniorChai/sql-motorcycle-sales-revenue
cd sql-motorcycle-sales-revenue
pip install pandas
python run_query.py
```

No database file needed — `run_query.py` loads `sales.csv` into an in-memory SQLite database and runs the query automatically.

---
*Part of my Data Analytics Portfolio — [github.com/JuniorChai](https://github.com/JuniorChai)*
