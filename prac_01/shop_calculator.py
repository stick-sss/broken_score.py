total = 0
items = int(input("Number of items: "))
for i in range(items):
    price = float(input("Price of item: "))
    while price < 0:
        print("Invalid number of items!")
        price = float(input("Price of item: "))
    total += price
if total > 100:
    final_price = total * 0.9
print(f"Total price for {items} is ${final_price:.2f}")