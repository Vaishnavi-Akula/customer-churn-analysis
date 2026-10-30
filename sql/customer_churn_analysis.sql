-- =====================================================
-- CUSTOMER CHURN ANALYSIS
-- Project: Customer Churn Analysis
-- Database: MySQL
-- Table: customer_churn_cleaned
-- =====================================================


-- 1. View sample customer records
SELECT *
FROM customer_churn_cleaned
LIMIT 10;


-- 2. Check the total number of customers
SELECT
    COUNT(*) AS total_customers
FROM customer_churn_cleaned;


-- 3. Calculate overall customer churn rate
SELECT
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        AS customers_churned,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_rate_percentage
FROM customer_churn_cleaned;


-- 4. Analyze churn by contract type
SELECT
    Contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        AS customers_churned,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_rate_percentage
FROM customer_churn_cleaned
GROUP BY Contract
ORDER BY churn_rate_percentage DESC;


-- 5. Analyze churn by payment method
SELECT
    PaymentMethod,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        AS customers_churned,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_rate_percentage
FROM customer_churn_cleaned
GROUP BY PaymentMethod
ORDER BY churn_rate_percentage DESC;


-- 6. Analyze churn by customer tenure
SELECT
    CASE
        WHEN tenure <= 12 THEN '0-12 Months'
        WHEN tenure <= 24 THEN '13-24 Months'
        WHEN tenure <= 48 THEN '25-48 Months'
        ELSE '49-72 Months'
    END AS tenure_group,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        AS customers_churned,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_rate_percentage
FROM customer_churn_cleaned
GROUP BY tenure_group
ORDER BY
    CASE tenure_group
        WHEN '0-12 Months' THEN 1
        WHEN '13-24 Months' THEN 2
        WHEN '25-48 Months' THEN 3
        ELSE 4
    END;


-- 7. Compare monthly charges by churn status
SELECT
    Churn,
    COUNT(*) AS total_customers,
    ROUND(AVG(MonthlyCharges), 2) AS average_monthly_charges,
    ROUND(MIN(MonthlyCharges), 2) AS minimum_monthly_charges,
    ROUND(MAX(MonthlyCharges), 2) AS maximum_monthly_charges
FROM customer_churn_cleaned
GROUP BY Churn;


-- 8. Analyze churn by internet service
SELECT
    InternetService,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        AS customers_churned,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_rate_percentage
FROM customer_churn_cleaned
GROUP BY InternetService
ORDER BY churn_rate_percentage DESC;


-- 9. Compare churn between senior and non-senior customers
SELECT
    SeniorCitizen,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        AS customers_churned,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_rate_percentage
FROM customer_churn_cleaned
GROUP BY SeniorCitizen
ORDER BY SeniorCitizen;


-- 10. Identify high-risk customer segments
SELECT
    Contract,
    PaymentMethod,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        AS customers_churned,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_rate_percentage
FROM customer_churn_cleaned
GROUP BY Contract, PaymentMethod
HAVING COUNT(*) >= 30
ORDER BY churn_rate_percentage DESC;