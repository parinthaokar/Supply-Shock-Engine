import mysql.connector
from mysql.connector import Error, errorcode
import json
import os
from dotenv import load_dotenv

load_dotenv()
try:
    with open("products_raw.json", "r") as file:
        json_data = json.load(file)
except Exception as e:
    print(f"Error reading JSON file: {e}")
    json_data = None

if json_data:
    connection = None
    try:
        connection = mysql.connector.connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_NAME")
        )
        if connection.is_connected():
            cursor = connection.cursor()

            query = "INSERT INTO products (product_id, category, base_price) VALUES (%s, %s, %s)"

            data_to_insert = [(row["id"], row["category"], row["price"]) for row in json_data]

            cursor.executemany(query, data_to_insert)
            connection.commit()
            
            print(f"Successfully inserted {cursor.rowcount} rows into the database.")

    except Error as e:
        print(f"Failed to insert data into MySQL: {e}")
        if connection and connection.is_connected():
            connection.rollback()

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")