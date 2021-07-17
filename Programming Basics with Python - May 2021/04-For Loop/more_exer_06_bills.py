months_amount=int(input())
electricity_cost_total=0
water_cost_total=0
internet_cost_total=0
others_cost_total=0

for month in range (months_amount):
    electricity_cost=float(input())
    water_cost=20
    internet_cost=15
    others_cost=(electricity_cost+water_cost+internet_cost)*1.2

    electricity_cost_total+=electricity_cost
    water_cost_total+=water_cost
    internet_cost_total+=internet_cost
    others_cost_total+=others_cost

average_cost_total=(electricity_cost_total+water_cost_total+internet_cost_total+others_cost_total)/months_amount

print(f"Electricity: {electricity_cost_total:.2f} lv")
print(f"Water: {water_cost_total:.2f} lv")
print(f"Internet: {internet_cost_total:.2f} lv")
print(f"Other: {others_cost_total:.2f} lv")
print(f"Average: {average_cost_total:.2f} lv")