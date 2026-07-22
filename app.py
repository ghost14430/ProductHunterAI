def search_products():
    print("\nSearching for products...\n")

    products = [
        {"name": "Wireless Earbuds", "buy": 150, "sell": 299},
        {"name": "LED Strip Lights", "buy": 80, "sell": 199},
        {"name": "Phone Holder", "buy": 35, "sell": 99},
    ]

    for item in products:
        profit = item["sell"] - item["buy"]
        print(f"Product : {item['name']}")
        print(f"Buy     : R{item['buy']}")
        print(f"Sell    : R{item['sell']}")
        print(f"Profit  : R{profit}")
        print("-" * 30)

print("=== PRODUCT HUNTER AI ===")
product = input("What product are you looking for? ")

print(f"\nSearching for '{product}'...")
search_products()
