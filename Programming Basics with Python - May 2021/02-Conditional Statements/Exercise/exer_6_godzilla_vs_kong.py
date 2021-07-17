movie_budget = float(input())

amount_extras = int(input())

price_costume_single = float(input())

price_stage_set = float(movie_budget * 0.1)

price_costume_total_nominal = (price_costume_single * amount_extras)

price_costume_total = float(0)

if amount_extras <= 150:
    price_costume_total = price_costume_total_nominal

elif amount_extras:
    price_costume_total = (price_costume_total_nominal * 0.9)

total_cost = (price_stage_set + price_costume_total)

if total_cost <= movie_budget:
    money_left = (movie_budget - total_cost)
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")

else:
    money_needed = (total_cost - movie_budget)
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
