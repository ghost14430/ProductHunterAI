print("=================================")
print("      PRODUCT HUNTER AI")
print("=================================")

product = input("Enter product name: ")

print("\nSearching for:", product)
print("Please wait...\n")

products = [
    {"name": "Wireless Earbuds", "buy": 150, "sell": 299},
    {"name": "LED Strip Lights", "buy": 80, "sell": 199},
    {"name": "Phone Holder", "buy": 35, "sell": 99}
]

print("Recommended Products:")
print("---------------------")

for item in products:
    profit = item["sell"] - item["buy"]
    print(f"{item['name']}")
    print(f" Buy Price : R{item['buy']}")
    print(f" Sell Price: R{item['sell']}")
    print(f" Profit    : R{profit}")
    print()
