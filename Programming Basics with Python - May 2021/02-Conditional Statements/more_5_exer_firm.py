import math

hours_req = int(input())

days_available = int(input())

amount_workers_extra = int(input())

days_working = float(days_available * .9)

hours_working_regular = float(days_working * 8)

hours_working_extra = float(amount_workers_extra * days_available * 2)

hours_working_total = float(math.floor(hours_working_extra + hours_working_regular))

if hours_working_total < hours_req:
    hours_insuff = int(hours_req - hours_working_total)
    print(f"Not enough time!{hours_insuff} hours needed.")
else:
    hours_left = int(hours_working_total - hours_req)
    print(f"Yes!{hours_left} hours left.")
