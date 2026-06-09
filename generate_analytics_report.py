import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

query = """select s.region, COUNT(p.product_id) as total_products, SUM(i.stock_quantity * p.base_price) as total_inventory_value, AVG(i.stock_quantity) as average_stock_level
from products p
join inventory i on p.product_id = i.product_id
join suppliers s on i.supplier_id = s.supplier_id
group by region"""

cursor.execute(query)
rows = cursor.fetchall()

print("====================================================")
print("        GLOBAL SUPPLY CHAIN EXECUTIVE REPORT        ")
print("====================================================\n")

for r in rows:
    region = r[0]
    total_products = r[1]
    total_val = r[2]
    avg_stock = r[3]
    
    print(f"REGION: {region}")
    print(f"   - Total Monitored Products: {total_products}")
    print(f"   - Total Portfolio Value At Risk: ${total_val:,.2f}") # Rounds to 2 decimals and adds commas!
    print(f"   - Average Regional Warehouse Stock: {avg_stock:.1f} units")
    print("-" * 52)

cursor.close()
conn.close()
