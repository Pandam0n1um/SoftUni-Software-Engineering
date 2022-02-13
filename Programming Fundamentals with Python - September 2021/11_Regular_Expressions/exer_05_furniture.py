import re

pattern = r"^>>(?P<Item>[a-zA-Z]+)<<(?P<Price>[0-9]+\.?[0-9]+)!(?P<Qty>[0-9]+)$"

items = {}
total_cost = 0
print("Bought furniture:")
while True:
    command = input()
    if command == "Purchase":
        break
    valid_item = re.search(pattern, command)
    if valid_item:
        current_product = valid_item.groupdict()
        print(f"{current_product['Item']}")
        curr_qty = int(current_product['Qty'])
        curr_price = float(current_product['Price'])
        total_cost += (curr_qty * curr_price)
print(f"Total money spend: {total_cost:.2f}")