def shopping_list(leva, **products):
    purchases = []
    if leva < 100:
        return f"You do not have enough budget."
    for item, data in products.items():
        price = float(data[0])
        count = int(data[1])
        curr_price = price * count
        if curr_price <= leva:
            leva -= curr_price
            purchases.append(f"You bought {item} for {curr_price:.2f} leva.")
        if len(purchases) == 5:
            break
    return '\n'.join(purchases)


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print()
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print()
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
