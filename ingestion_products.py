import requests
import json

url = "https://fakestoreapi.com/products"

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        # CHANGED: 'data' inside the loop changed to 'd'
        cleaned_products = [
            {
                "id": d["id"],
                "category": d["category"],
                "price": d["price"]
            }
            for d in data
        ]

        print(f"\nSuccessfully pulled {len(cleaned_products)} products.")
        
        with open('products_raw.json', 'w') as f:
            json.dump(cleaned_products, f, indent= 4)
        
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"A connection error occurred: {e}")

