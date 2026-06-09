import mysql.connector
import random
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


query = "SELECT product_id,base_price from products"
cursor.execute(query)
rows = cursor.fetchall()



for r in rows:
    id = r[0]
    price = r[1]
    supplier_id = random.randint(1,4)
    if price > 100:
        stock_quantity = random.randint(10, 50)
    else:
        stock_quantity = random.randint(100, 500)
        
    cursor.execute("INSERT INTO inventory (product_id,supplier_id,stock_quantity) VALUES (%s, %s, %s)", (id,supplier_id,stock_quantity))
    conn.commit()

print("Sucessful")

cursor.close()
conn.close()