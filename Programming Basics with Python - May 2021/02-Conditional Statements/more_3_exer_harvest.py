import math

vineyard_area = int(input())

yield_sqm = float(input())

amount_wine_req = int(input())

amount_workers = int(input())

amount_wine_result = float(vineyard_area * .4 * yield_sqm / 2.5)

if amount_wine_result < amount_wine_req:
    amount_wine_insuff = float((amount_wine_req - amount_wine_result))
    print(f"It will be a tough winter! More {math.floor(amount_wine_insuff)} liters wine needed.")

else:
    amount_wine_excessive = float(amount_wine_result - amount_wine_req)
    amount_wine_per_worker = float(amount_wine_excessive / amount_workers)
    print(f"Good harvest this year! Total wine: {math.floor(amount_wine_result)} liters.")
    print(f"{math.ceil(amount_wine_excessive)} liters left -> {math.ceil(amount_wine_per_worker)} liters per person.")
