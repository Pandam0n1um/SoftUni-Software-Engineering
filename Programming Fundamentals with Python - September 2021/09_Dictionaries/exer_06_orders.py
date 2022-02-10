dict_products = {}
while True:
    command = input()
    if command == "buy":
        break
    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if product not in dict_products:
        dict_products[product] = {"price": price, "quantity": quantity}
    else:
        dict_products[product]["price"] = price
        dict_products[product]["quantity"] += quantity

for key, value in dict_products.items():
    tot_price = value['price'] * value['quantity']
    print(f"{key} -> {tot_price:.2f}")
