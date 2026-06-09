CREATE DATABASE supply_chain_db;
USE supply_chain_db;

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    category VARCHAR(100),
    base_price DECIMAL(10, 2)
);

-- 1. Create the Suppliers Table
CREATE TABLE suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_name VARCHAR(100),
    region VARCHAR(50),          -- e.g., 'East Asia', 'Europe', 'North America'
    risk_status VARCHAR(20)      -- 'Active', 'Delayed', or 'Critical Shutdown'
);

-- 2. Create the Inventory Table (Links products to suppliers and tracks stock)
CREATE TABLE inventory (
    product_id INT PRIMARY KEY,
    supplier_id INT,
    stock_quantity INT,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);