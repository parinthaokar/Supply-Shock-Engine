# ⚡ Global Supply Chain Ingestion & Dynamic Pricing Engine

An end-to-end data engineering pipeline built with Python and MySQL that automates API data ingestion, tracks inventory through a normalized relational schema, simulates an East Asia supplier crisis, and dynamically reprices products using warehouse scarcity metrics.

---

## 📌 Project Overview

This project models a real-world macroeconomic disruption scenario. When a major supplier region experiences a shutdown, organizations must rapidly assess operational inventory levels and adjust pricing strategies to protect profit margins.

The system accomplishes this through a custom operational pipeline that:

1. **Ingests** external product data from a REST API into a raw JSON file.
2. **Seeds and standardizes** the data into a normalized MySQL database.
3. **Simulates a regional supply crisis** by altering supplier risk attributes.
4. **Triggers a dynamic pricing algorithm** based on inventory scarcity.
5. **Generates executive-level analytics** summarizing portfolio risk exposure.

---

## 🏗️ System Architecture

```text
┌─────────────────────┐
│ External Product API│
└──────────┬──────────┘
           │ (requests)
           ▼
   JSON Landing Zone
 (products_raw.json)
           │
           ▼
┌──────────────────────────────────────┐
│  Normalized MySQL Relational Store   │
├──────────────────────────────────────┤
│ products ─── join ─── inventory      │
│                         │            │
│                       join           │
│                         │            │
│                      suppliers       │
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
 Executive Analytics Summary
 (GROUP BY / SUM / AVG)
```

---

## 🚀 System Features

### 🌍 REST API Data Ingestion

Built an automated ingestion script (`ingestion_products.py`) that:

* Connects to an external REST API
* Retrieves product datasets
* Filters unnecessary attributes
* Standardizes product metadata
* Writes structured JSON to a local landing zone

---

### 🗄️ Normalized Relational Database Design

Designed a normalized MySQL schema to preserve referential integrity and reduce data redundancy.

#### Products

Stores product identifiers, names, and pricing information.

#### Suppliers

Stores vendor metadata, regional classifications, and operational risk statuses.

#### Inventory

Maintains stock quantities while linking products and suppliers through foreign-key relationships.

This design enables efficient joins, scalable analytics, and strong relational consistency.

---

### ⚡ Event-Driven Crisis Simulation & Dynamic Pricing

The `simulate_supply_shock.py` module models a real-time supply chain disruption.

#### Crisis Simulation

* Identifies suppliers operating within the **East Asia** region.
* Updates supplier status to **Critical Shutdown**.
* Evaluates inventory availability across impacted products.

#### Dynamic Pricing Logic

Products are repriced according to inventory scarcity:

* Inventory < 150 units → **50% price increase**
* Inventory ≥ 150 units → **20% price increase**

#### Financial Precision

The pricing engine uses Python's `decimal.Decimal` type to eliminate floating-point precision errors during financial calculations.

#### Transaction Optimization

All pricing adjustments are processed in memory and committed through a single database transaction using:

```python
conn.commit()
```

This minimizes database overhead and ensures transactional consistency.

---

## 📊 Executive Analytics Layer

The analytics engine (`generate_analytics_report.py`) generates business intelligence metrics directly from the operational database.

Key metrics include:

* Total monitored products
* Regional inventory counts
* Portfolio value at risk
* Average warehouse stock levels

The reporting layer utilizes:

* Multi-table SQL joins
* Aggregate functions (`SUM`, `AVG`, `COUNT`)
* Regional grouping (`GROUP BY`)
* Inventory valuation calculations

---

## 🛠️ Tech Stack

| Category                 | Technology             |
| ------------------------ | ---------------------- |
| Language                 | Python 3               |
| Database                 | MySQL                  |
| API Integration          | Requests               |
| Database Driver          | mysql-connector-python |
| Configuration Management | python-dotenv          |
| Financial Precision      | decimal.Decimal        |
| Data Format              | JSON                   |
| Query Language           | SQL                    |

---

## 🔒 Security Architecture

This project follows production-style credential management practices.

### Environment Variable Isolation

Database credentials are stored separately from application code using a local `.env` file.

```env
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=supply_chain_db
```

### Repository Protection

The repository includes a `.gitignore` file to prevent accidental exposure of credentials and local cache files.

```gitignore
.env
__pycache__/
*.pyc
```

---

## 📈 Sample Executive Report

```text
====================================================
        GLOBAL SUPPLY CHAIN EXECUTIVE REPORT
====================================================

🌍 REGION: East Asia

   - Total Monitored Products: 7
   - Total Portfolio Value At Risk: $14,842.50
   - Average Regional Warehouse Stock: 112.4 units

----------------------------------------------------
```

---

## 📂 Project Structure

```text
supply_shock_engine/
│
├── .env.example
├── .gitignore
├── db_connection.py
├── ingestion_products.py
├── seed_operational_data.py
├── simulate_supply_shock.py
├── generate_analytics_report.py
│
├── products_raw.json
└── supply_chain_db.sql
```

---

## ⚙️ Installation & Deployment

### Clone the Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/supply_shock_engine.git

cd supply_shock_engine
```

### Install Dependencies

```bash
pip install mysql-connector-python python-dotenv requests
```

### Configure Environment Variables

Copy `.env.example` and rename it to `.env`.

Populate it with your local database credentials:

```env
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=supply_chain_db
```

### Execute the Pipeline

Run each component sequentially:

```bash
python3 ingestion_products.py
python3 seed_operational_data.py
python3 simulate_supply_shock.py
python3 generate_analytics_report.py
```

---

## 🎯 Technical Skills Demonstrated

### Data Engineering

* ETL Pipeline Development
* REST API Integration
* JSON Processing
* Data Standardization

### Database Engineering

* Relational Schema Design
* Foreign Key Relationships
* SQL Joins & Aggregations
* Transaction Management

### Backend Development

* Event-Driven Processing
* Dynamic Pricing Algorithms
* Financial Precision Handling
* Secure Configuration Management

### Analytics Engineering

* KPI Development
* Portfolio Risk Analysis
* Business Intelligence Reporting
* Operational Metrics

---
