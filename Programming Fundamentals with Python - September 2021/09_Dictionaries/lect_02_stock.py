elements = input().split()
searched=input().split()
stock = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = int(elements[i + 1])
    stock[key] = value

for product in searched:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")