
import requests

API_URL = "https://api.digikala.com/v1/search/?q={query}"

choice = input("Enter your product (ps5 or xbox?): ").lower()

if choice == "ps5":
    query = "ps5"
elif choice == "xbox":
    query = "xbox"
else:
    print("Invalid selection.")
    exit()

url = API_URL.format(query=query)
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

if response.status_code != 200:
    print(f"Error: API returned status code {response.status_code}")
    exit()

data = response.json()
products = data.get("data", {}).get("products", [])

if not products:
    print("No products found.")
    exit()

print("------ Results ------")

for i, product in enumerate(products[:5], start=1):
    title = product.get("title_fa", "Unknown")
    price_info = product.get("default_variant", {}).get("price", {})
    price = price_info.get("selling_price", 0)
    price_str = f"{price:,} Toman" if price else "Unavailable"

    product_url = f"https://www.digikala.com/product/dkp-{product.get('id')}/"

    print(f"{i}. Product name: {title}")
    print(f"   Price: {price_str}")
    print(f"   Link: {product_url}")
    print("----------------------")

print("Information received successfully.")
