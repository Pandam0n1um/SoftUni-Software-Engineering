duration_days = int(input())

count_confectioner = int(input())

count_cakes = int(input())

count_gaufres = int(input())

count_creppes = int(input())

cake_cost = 45

gaufre_cost = 5.80

creppe_cost = 3.20

total_cakes_cost = float(count_cakes * cake_cost)

total_gaufres_cost = float(count_gaufres * gaufre_cost)

total_creppes_cost = float(count_creppes * creppe_cost)

total_cost_day = float(total_cakes_cost + total_gaufres_cost + total_creppes_cost) * count_confectioner

total_cost = float(total_cost_day * duration_days)

total_profit = float(total_cost * (1-1/8))

print(total_profit)

print(total_cost*total_cost)


#

duration_days = int(input())

count_confectioner = int(input())

count_cakes = int(input())

count_gaufres = int(input())

count_creppes = int(input())

total_cakes_cost = float(count_cakes * 45)

total_gaufres_cost = float(count_gaufres * 5.8)

total_creppes_cost = float(count_creppes * 3.2)

total_cost_day = float(total_cakes_cost + total_gaufres_cost + total_creppes_cost) * count_confectioner

total_cost = float(total_cost_day * duration_days)

total_profit = float(total_cost * (1-1/8))

print(total_profit)

