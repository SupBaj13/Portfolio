print("Beckett Pizza Plaza 4-for-3 Offer")
print("=================================")

def valid_price(amount):
    while True:
        try:
            price = float(input(amount))
            if price <= 0:
                print("Please enter a valid price!")
                continue
            return price
        except ValueError:
            print("Please enter a valid price!")

prices = []
for i in range(1, 5):
    prices.append(valid_price(f"Enter Price of Pizza #{i}: "))

prices.sort()
total_charged = sum(prices[:3])
full_total = sum(prices)
discount_pct = (full_total - total_charged) / full_total * 100

print(f"Order Total is £{total_charged:.2f}, a fabulous discount of {discount_pct:.0f}%!")
