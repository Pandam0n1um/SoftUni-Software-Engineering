count_days = int(input())
count_hours = int(input())
total_cost = 0
for days in range(1, count_days + 1):
    daily_cost = 0
    if days % 2 == 0:
        is_day_even = True
    else:
        is_day_even = False
    for hours in range(1, count_hours + 1):
        if hours % 2 == 0:
            is_hour_even = True
        else:
            is_hour_even = False
        if is_day_even and not is_hour_even:
            daily_cost += 2.50
        elif not is_day_even and is_hour_even:
            daily_cost += 1.25
        else:
            daily_cost += 1.00

    print(f"Day: {days} - {daily_cost:.2f} leva")
    total_cost += daily_cost
print(f"Total: {total_cost:.2f} leva")
