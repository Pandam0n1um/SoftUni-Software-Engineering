holiday_cost = float(input())
starting_money = float(input())

total_money = starting_money
consecutive_spending_day_counter = 0
total_day_counter = 0

is_money_enough = True

while total_money < holiday_cost:
    if consecutive_spending_day_counter == 5:
        is_money_enough = False
        break
    total_day_counter+=1
    daily_action = str(input())
    daily_sum = float(input())
    if daily_action == "spend" and total_money<daily_sum:
        total_money=0
        consecutive_spending_day_counter += 1
        continue
    elif daily_action == "spend":
        total_money -= daily_sum
        consecutive_spending_day_counter += 1
        continue
    else:
        total_money += daily_sum
        consecutive_spending_day_counter = 0

if is_money_enough:
    print(f"You saved the money for {total_day_counter} days.")
else:
    print(f"You can't save the money.")
    print(f"{total_day_counter}")