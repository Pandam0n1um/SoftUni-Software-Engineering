total_rent = int(input())

cake_cost = float(total_rent * 0.2)

drinks_cost = float(cake_cost * 0.55)

animator_cost = float(total_rent / 3)

total_cost = float(total_rent + cake_cost + drinks_cost + animator_cost)

print(total_cost)
