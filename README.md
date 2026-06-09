# ⚡ Global Supply Chain Ingestion & Dynamic Pricing Engine

An end-to-end data engineering pipeline in Python and MySQL that automates API data ingestion, tracks inventory across a normalized relational schema, simulates an East Asia supplier crisis, and executes algorithmic dynamic pricing based on warehouse scarcity metrics.

## 📌 Project Overview
This project models a real-world macroeconomic disruption scenario. When a major supplier region undergoes a shutdown, organizations must rapidly assess operational inventory levels and dynamically alter pricing strategies to defend profit margins.

This system achieves this through a custom operational pipeline that:
1. **Ingests** external product data from a REST API into a raw JSON file.
2. **Seeds and standardizes** the data into a normalized, 3-table MySQL database.
3. **Simulates a regional supply crisis** by altering vendor risk attributes on the fly.
4. **Triggers a custom pricing algorithm** to hike prices based on inventory counts.
5. **Aggregates operational metrics** to output an executive portfolio financial risk summary.

---

## 🏗️ System Architecture
```text
┌─────────────────────┐
│ External Product API│
└──────────┬──────────┘
           │ (requests)
           ▼
   JSON Landing Zone (products_raw.json)
           │
           ▼
┌──────────────────────────────────────┐
│  Normalized MySQL Relational Store   │
├──────────────────────────────────────┤
│ products ─── join ─── inventory      │
│                         │            │
│                       join           │
│                         │            │
│                       suppliers      │
└──────────────────┬───────────────────┘
                   │
                   ▼
    Event-Driven East Asia Shutdown 
                   │
                   ▼
 Dynamic Pricing Engine (decimal.Decimal)
                   │
                   ▼
  Single-Batch Transaction Commit
                   │
                   ▼
Executive Analytics Summary (GROUP BY / SUM)

🚀 Actual System Features
🌍 REST API Data Ingestion
Built an automated ingestion script (ingestion_products.py) that handles HTTP handshakes, queries an external REST API endpoint, filters raw JSON payloads down to necessary metadata attributes, and writes the stream to a local raw landing zone.

🗄️ Normalized Relational Database Design
Modeled a relational schema in MySQL to preserve referential integrity. The store consists of three highly coupled tables joined together via structured foreign keys:

products: Maintains base prices and item identifiers.

suppliers: Stores vendor metadata, regional boundaries, and operational risk states.

inventory: Maps physical tracking variables, joining specific products to their respective suppliers alongside localized unit balances.

⚡ Event-Driven Crisis Simulation & Dynamic Pricing
Simulates a real-time macroeconomic shock event (simulate_supply_shock.py).

Intercepts and flags all vendors situated within the 'East Asia' region, updating their status to 'Critical Shutdown'.

Scans live inventory logs to evaluate scarcity metrics.

Implements a scarcity-based feedback loop: low-stock items (< 150 units) receive a 50% dynamic price surge, while high-stock items (>= 150 units) receive a 20% surge.

Financial Precision Design: Leverages Python’s native decimal.Decimal module to completely eliminate floating-point rounding errors during multi-decimal multiplication, ensuring production-grade accuracy for financial accounting.

Batch Transaction Optimization: Executes all updates in memory and relies on a singular conn.commit() after loop termination to minimize network overhead and safely write changes to disk.

📊 Aggregated Executive Analytics
Uses a heavy analytical aggregation query inside generate_analytics_report.py to extract high-level KPIs straight to the terminal interface. Utilizes multi-table relational joins, arithmetic evaluations (stock_quantity * base_price), and optimized database GROUP BY operations.

🛠️ Tech Stack
Language: Python 3

Database Engine: MySQL Server

API Integration: requests

Drivers: mysql-connector-python

Configuration & Security: python-dotenv

Financial Modeling: decimal

🔒 Security Architectures
This project strictly adheres to production-grade credential management practices:

Environment Variable Isolation: Database hosts, root usernames, and access passwords are decoupled from codebase source files and isolated in a localized .env configuration file.

Git Repository Protection: Configured a native .gitignore file to actively prevent the submission of hidden credentials or local caches (__pycache__/) to public version control.

📈 Live Terminal Executive Report Output
Plaintext
====================================================
        GLOBAL SUPPLY CHAIN EXECUTIVE REPORT        
====================================================

🌍 REGION: East Asia
   - Total Monitored Products: 7
   - Total Portfolio Value At Risk: $14,842.50
   - Average Regional Warehouse Stock: 112.4 units
----------------------------------------------------
📂 Project Structure
Plaintext
supply_shock_engine/
│
├── .env.example                  # Template file for local DB setup
├── .gitignore                    # Ensures .env stays hidden on your machine
├── db_connection.py              # Central database configuration utility
├── ingestion_products.py         # Step 1: API ingestion engine
├── seed_operational_data.py      # Step 2: Relational seeding script
├── simulate_supply_shock.py      # Step 3: Crisis & dynamic pricing logic
├── generate_analytics_report.py  # Step 4: Analytical executive KPI script
│
├── products_raw.json             # Milestone 1 raw JSON file dump
└── supply_chain_db.sql           # Database schema & layout exports
⚙️ Installation & Deployment
Clone the repository:

Bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/supply_shock_engine.git](https://github.com/YOUR_GITHUB_USERNAME/supply_shock_engine.git)
cd supply_shock_engine
Install core dependencies:

Bash
pip install mysql-connector-python python-dotenv requests
Configure Environment Variables:

Duplicate .env.example and rename the copy to .env

Populate the file with your local database credentials:

Plaintext
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=supply_chain_db
Execute Pipeline Lifecycle Sequentially:

Bash
python3 ingestion_products.py
python3 seed_operational_data.py
python3 simulate_supply_shock.py
python3 generate_analytics_report.py
🎯 Core Technical Skills Exhibited
Data Pipelines: End-to-end local ETL, raw data file processing, JSON parsing.

Database Engineering: Normalized Relational Database Design, SQL Joins & Aggregations, Transaction Commit Auditing.

Backend Programming: Event-Driven Logic Flow, Error-free Data Type Casting (Decimal), Secure Infrastructure Design (dotenv).

👨‍💻 Author
Parin Thaokar Data Engineering • Analytics Engineering • Backend Systems
