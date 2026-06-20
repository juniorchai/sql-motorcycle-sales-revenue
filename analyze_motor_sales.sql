-- ============================================================
-- Motorcycle Parts Wholesale Revenue Analysis
-- Dataset : sales.csv (1,000 orders, 11 columns)
-- Goal    : Calculate net revenue per product line, month,
--           and warehouse for Wholesale orders only
-- Period  : June - August 2021
-- Formula : net_revenue = ROUND(SUM(total) - SUM(payment_fee), 2)
-- ============================================================

SELECT
    product_line,
    CASE
        WHEN EXTRACT('month' FROM date) = 6 THEN 'June'
        WHEN EXTRACT('month' FROM date) = 7 THEN 'July'
        WHEN EXTRACT('month' FROM date) = 8 THEN 'August'
    END AS month,
    warehouse,
    ROUND(SUM(total) - SUM(payment_fee), 2) AS net_revenue  -- Net after payment fees

FROM sales
WHERE client_type = 'Wholesale'                             -- Wholesale orders only
GROUP BY product_line, month, warehouse
ORDER BY product_line, month, net_revenue DESC;
