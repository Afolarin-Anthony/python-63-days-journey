# Product price list

products = [
    ("Laptop", 999.99),
    ("Mouse", 25.50),
    ("Keyboard", 60.00)
]

print(f"{'Product':<15}{'Price':>10}")
print("-" * 25)

for product, price in products:
    print(f"{product:<15}{price:>10.2f}")
