strawberry_price = float(input())

banana_amount = float(input())

orange_amount = float(input())

raspberry_amount = float(input())

strawberry_amount = float(input())

raspberry_price = float(strawberry_price * 0.5)

orange_price = float(raspberry_price * 0.6)

banana_price = float(raspberry_price * 0.2)

strawberry_cost = float(strawberry_price * strawberry_amount)

raspberry_cost = float(raspberry_amount * raspberry_price)

orange_cost = float(orange_price * orange_amount)

banana_cost = float(banana_price * banana_amount)

total_cost = (strawberry_cost + raspberry_cost + orange_cost + banana_cost)

print(total_cost)
