import mysql.connector
from decimal import Decimal
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

cursor.execute("""UPDATE suppliers SET risk_status = 'Critical Shutdown'
WHERE region = 'East Asia'""")

conn.commit()

query = """select p.product_id, p.base_price, s.supplier_id, s.risk_status, i.stock_quantity from
products p
join inventory i on p.product_id = i.product_id
join suppliers s on i.supplier_id = s.supplier_id
WHERE region = 'East Asia'"""

cursor.execute(query)
rows = cursor.fetchall()

for r in rows: 
    id = r[0]
    price = r[1]
    stock_quanitity = r[4]

    if stock_quanitity < 150:
        newPrice = price * Decimal('1.50')
        print(f"CRITICAL ALERT:Product: {id}, Stock: {stock_quanitity}, Price Adjusted from price {price} to {newPrice} ")
    elif stock_quanitity >= 150:
        newPrice = price * Decimal('1.20')
        print(f"CRITICAL ALERT:Product: {id}, Stock: {stock_quanitity}, Price Adjusted from price {price} to {newPrice} ")
    cursor.execute("""UPDATE products SET base_price = %s WHERE product_id = %s""", (newPrice,id))
conn.commit()

print("Database successfully updated with dynamic surge prices!")
cursor.close()
conn.close()