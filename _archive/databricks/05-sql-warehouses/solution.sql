-- Task 5: SQL Warehouses — Solutions
-- Exercise 1: Databricks SQL analytics queries
-- Table: sales(order_id, order_date, customer_id, product_id, category, quantity, unit_price, discount, region)

-- 1a. Year-over-year revenue growth by region


-- 1b. Running total of daily revenue (window function)


-- 1c. Top 5 products by revenue in each category (use QUALIFY)


-- 1d. Customer cohort analysis: revenue by signup month cohort
-- Assume a customers table with customer_id, signup_date


-- 1e. Moving 30-day average order value


-- ============================================================
-- Exercise 2: Query Optimization

-- 2a. Slow version: full scan on 10TB events table

-- 2b. Optimized version (describe partitioning/Z-ORDER setup + rewritten query)


-- 2c. What to look for in EXPLAIN output (write as comments)
