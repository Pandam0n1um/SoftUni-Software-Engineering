import math

count_days=int(input())

amount_food_provided=int(input())

amount_food_per_day_dog=float(input())

amount_food_per_day_cat=float(input())

amount_food_per_day_turtle=float(input())

amount_food_req=(count_days*(amount_food_per_day_dog+amount_food_per_day_cat+amount_food_per_day_turtle*0.001))

if amount_food_req<=amount_food_provided:
    amount_food_remaining=(math.floor(amount_food_provided-amount_food_req))
    print(f"{amount_food_remaining} kilos of food left.")
else:
    amount_food_insuff=(math.ceil(amount_food_req-amount_food_provided))
    print(f"{amount_food_insuff} more kilos of food are needed.")