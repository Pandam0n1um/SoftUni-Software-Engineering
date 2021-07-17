eur_to_bgn = 1.94

vegetable_price = float(input())

fruit_price = float(input())

vegetable_amount = float(input())

fruit_amount = float(input())

vegetable_cost = float(vegetable_amount * vegetable_price)

fruit_cost = float(fruit_amount * fruit_price)

total_cost_bgn = vegetable_cost + fruit_cost

total_cost_eur = total_cost_bgn / eur_to_bgn

print(f"{total_cost_eur:.2f}")
