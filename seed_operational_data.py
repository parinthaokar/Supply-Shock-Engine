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

supplier_list = [("Apex Electronics", "East Asia", "Active"),("Continental Logistics", "Europe", "Active"),("North American Supply Chain", "North America", "Active"),("Pacific Freight Partners", "East Asia", "Active")]

query = "INSERT INTO suppliers (supplier_name, region, risk_status) VALUES (%s, %s, %s)"

cursor.executemany(query, supplier_list)
conn.commit()
print("Sucessfully Pushed suppliers")

cursor.close()
conn.close()
print("MySQL connection is closed.")