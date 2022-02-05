def calculate_total_price(product, quantity):
    if product == "water":
        return quantity * 1
    elif product == "coffee":
        return quantity * 1.5
    elif product == "coke":
        return quantity * 1.4
    elif product == "snacks":
        return quantity * 2


type_product = input()
amount = int(input())

total_amount = calculate_total_price(type_product, amount)
print(f"{total_amount:.2f}")