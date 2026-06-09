# ⚡ Global Supply Chain Ingestion & Dynamic Pricing Engine

An end-to-end, event-driven data engineering pipeline that simulates a macroeconomic geopolitical crisis, evaluates real-time localized warehouse scarcity metrics, and dynamically re-prices global inventory using an automated algorithmic feedback loop.

## 🏗️ Architecture Overview
1. **Ingestion Layer:** Python `requests` engine extracting product assets from an external API, performing target attribute filtering, and outputting to a structured local JSON landing zone.
2. **Operational Relational Store:** Highly normalized MySQL multi-table relational schema maintaining strong relational integrity across core product, inventory tracking, and vendor entity dimensions.
3. **Event & Algorithmic Pricing Engine:** Event-driven transaction script simulating a region-wide supplier shutdown, recalculating unit pricing dynamically based on warehouse scarcity logic, and batch-committing updates back to the transactional layer using isolated type casting (`decimal.Decimal`) to eliminate precision loss.
4. **Analytics Layer:** Aggregated data extraction engine generating high-level business metrics (`SUM`, `AVG`, `COUNT`) using optimized relational joins to expose asset values at risk per global region.

## 💻 Tech Stack & Security Best Practices
* **Language:** Python 3
* **Database:** MySQL Server (Relational Schema Design)
* **Libraries:** `mysql-connector-python`, `python-dotenv`, `requests`, `decimal`
* **Security:** Implemented environment variable isolation (`.env` decouple via `.gitignore`) to secure operational infrastructure credentials, preventing credential leaks in public version control.

## 📊 Sample Executive Insights
```text
====================================================
        GLOBAL SUPPLY CHAIN EXECUTIVE REPORT        
====================================================
🌍 REGION: East Asia
   - Total Monitored Products: 7
   - Total Portfolio Value At Risk: $14,842.50
   - Average Regional Warehouse Stock: 112.4 units
----------------------------------------------------
🚀 Getting Started
Clone the repository:

Bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/supply_shock_engine.git](https://github.com/YOUR_GITHUB_USERNAME/supply_shock_engine.git)
cd supply_shock_engine
Install dependencies:

Bash
pip install mysql-connector-python python-dotenv requests
Set up your environment variables:

Duplicate .env.example and rename it to .env

Populate it with your local MySQL database credentials:

Plaintext
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=your_database_name
Run the components sequentially:

Bash
python3 ingestion_products.py
python3 seed_operational_data.py
python3 simulate_supply_shock.py
python3 generate_analytics_report.py

***
