# ⚡ Global Supply Chain Ingestion & Dynamic Pricing Engine

> An end-to-end data engineering platform that simulates global supply chain disruptions, evaluates warehouse scarcity in real time, and dynamically reprices inventory using event-driven business logic.

---

## 📌 Project Overview

Modern supply chains are highly vulnerable to geopolitical events, regional shutdowns, and inventory shortages. Organizations must rapidly assess operational risk and adjust pricing strategies to maintain profitability.

This project models a real-world supply chain disruption scenario through a complete data pipeline that:

* Ingests external product data from an API
* Stores operational data in a normalized MySQL database
* Simulates geopolitical supply shocks
* Dynamically reprices inventory based on scarcity
* Generates executive-level business intelligence reports

The system demonstrates core data engineering concepts including ETL development, relational database design, event-driven processing, transactional updates, and analytics reporting.

---

# 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │ External Product API │
                    └──────────┬──────────┘
                               │
                               ▼
                 ┌─────────────────────────┐
                 │ Python Ingestion Engine │
                 │ (requests + filtering)  │
                 └──────────┬──────────────┘
                            │
                            ▼
                  JSON Landing Zone
                            │
                            ▼
         ┌─────────────────────────────────────┐
         │ Normalized MySQL Operational Store  │
         ├─────────────────────────────────────┤
         │ Products                            │
         │ Vendors                             │
         │ Warehouses                          │
         │ Inventory                           │
         └───────────────┬─────────────────────┘
                         │
                         ▼
          Event-Driven Supply Shock Engine
                         │
                         ▼
            Dynamic Pricing Algorithm
                         │
                         ▼
           Transactional Database Updates
                         │
                         ▼
               Analytics Reporting Layer
                         │
                         ▼
         Executive Business Intelligence
```

---

# 🚀 Key Features

### 🌍 External Data Ingestion

Built a Python-based ingestion engine that:

* Connects to external REST APIs
* Extracts product metadata
* Filters required business attributes
* Stores clean datasets in a structured JSON landing zone
* Creates reproducible datasets for downstream processing

---

### 🗄️ Relational Data Modeling

Designed a highly normalized MySQL schema to maintain strong data integrity across operational entities.

Core dimensions include:

* Products
* Vendors
* Warehouses
* Inventory Tracking

Benefits:

* Reduced redundancy
* Improved query performance
* Strong referential integrity
* Scalable relational architecture

---

### ⚡ Event-Driven Supply Shock Simulation

Simulates a major geopolitical disruption where a supplier region becomes unavailable.

The engine:

1. Identifies affected inventory
2. Calculates updated stock availability
3. Evaluates warehouse scarcity
4. Triggers pricing adjustments
5. Commits transactional updates to the database

This models real-world supply chain volatility and operational risk.

---

### 💰 Dynamic Pricing Engine

A custom algorithm automatically adjusts product pricing based on inventory scarcity.

Example logic:

```python
if stock_level < 25:
    price *= 1.20
elif stock_level < 50:
    price *= 1.10
```

Key implementation details:

* Uses `decimal.Decimal` for financial precision
* Eliminates floating-point rounding errors
* Supports transactional batch updates
* Maintains pricing consistency across regions

---

### 📊 Analytics & Business Intelligence

Aggregates operational data into executive-level metrics using optimized SQL queries.

Metrics include:

* Total products monitored
* Average inventory levels
* Portfolio value at risk
* Regional exposure analysis
* Inventory concentration metrics

Built using:

```sql
SUM()
AVG()
COUNT()
GROUP BY
INNER JOIN
```

---

# 🛠️ Tech Stack

| Category               | Technology             |
| ---------------------- | ---------------------- |
| Language               | Python 3               |
| Database               | MySQL                  |
| API Integration        | Requests               |
| Database Connector     | mysql-connector-python |
| Environment Management | python-dotenv          |
| Financial Precision    | decimal.Decimal        |
| Data Storage           | JSON                   |
| Query Language         | SQL                    |

---

# 🔒 Security Best Practices

This project follows industry-standard credential management practices.

### Environment Variable Isolation

Sensitive database credentials are stored in a local `.env` file and excluded from version control.

Example:

```env
DB_HOST=localhost
DB_USER=username
DB_PASSWORD=password
DB_NAME=supply_chain_db
```

### Git Protection

```gitignore
.env
__pycache__/
*.pyc
```

Benefits:

* Prevents accidental credential exposure
* Keeps repositories secure
* Follows production-grade deployment practices

---

# 📈 Sample Executive Report

```text
====================================================
        GLOBAL SUPPLY CHAIN EXECUTIVE REPORT
====================================================

🌍 REGION: East Asia

   • Total Monitored Products: 7

   • Total Portfolio Value At Risk:
     $14,842.50

   • Average Regional Warehouse Stock:
     112.4 units

----------------------------------------------------

🌍 REGION: North America

   • Total Monitored Products: 12

   • Total Portfolio Value At Risk:
     $22,910.00

   • Average Regional Warehouse Stock:
     147.8 units

----------------------------------------------------

🌍 REGION: Europe

   • Total Monitored Products: 9

   • Total Portfolio Value At Risk:
     $18,330.25

   • Average Regional Warehouse Stock:
     98.7 units

====================================================
```

---

# 📂 Project Structure

```text
supply_shock_engine/
│
├── ingestion_products.py
├── seed_operational_data.py
├── simulate_supply_shock.py
├── generate_analytics_report.py
│
├── data/
│   └── products.json
│
├── sql/
│   └── schema.sql
│
├── .env.example
├── requirements.txt
├── README.md
│
└── screenshots/
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/supply_shock_engine.git

cd supply_shock_engine
```

Install dependencies:

```bash
pip install mysql-connector-python
pip install python-dotenv
pip install requests
```

---

# 🔧 Environment Setup

Create a local `.env` file:

```env
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=your_database
```

---

# ▶️ Running The Pipeline

Execute each stage sequentially:

### 1. Ingest Product Data

```bash
python3 ingestion_products.py
```

### 2. Seed Operational Database

```bash
python3 seed_operational_data.py
```

### 3. Simulate Supply Chain Disruption

```bash
python3 simulate_supply_shock.py
```

### 4. Generate Executive Analytics

```bash
python3 generate_analytics_report.py
```

---

# 🎯 Skills Demonstrated

### Data Engineering

* ETL Pipeline Development
* API Integration
* Data Transformation
* Data Quality Validation

### Database Engineering

* Relational Schema Design
* Database Normalization
* SQL Query Optimization
* Referential Integrity

### Backend Engineering

* Event-Driven Processing
* Transaction Management
* Financial Precision Handling
* Batch Operations

### Analytics Engineering

* KPI Generation
* Business Intelligence Reporting
* Aggregation Frameworks
* Operational Metrics

---

# 📚 Future Enhancements

Potential production-grade upgrades:

* Apache Airflow orchestration
* Kafka event streaming
* Docker containerization
* AWS S3 data lake integration
* dbt transformation layer
* Power BI dashboarding
* Real-time inventory monitoring
* Machine learning demand forecasting

---

# 👨‍💻 Author

**Parin Thaokar**

Data Engineering • Analytics Engineering • Backend Systems

Built to demonstrate practical ETL development, relational database design, event-driven architecture, and business intelligence workflows in a real-world supply chain scenario.
