amount_freights=int(input())
microbus_weight=0
lorry_weight=0
train_weight=0

for freight in range (amount_freights):
    current_freight_weight=int(input())
    if current_freight_weight<=3:
        microbus_weight+=current_freight_weight
    elif 4<=current_freight_weight<=11:
        lorry_weight+=current_freight_weight
    elif 12<=current_freight_weight:
        train_weight+=current_freight_weight

total_weight=microbus_weight+lorry_weight+train_weight
average_cost_tonne=(microbus_weight*200+lorry_weight*175+train_weight*120)/total_weight
microbus_relative=(microbus_weight/total_weight)*100
lorry_relative=(lorry_weight/total_weight)*100
train_relative=(train_weight/total_weight)*100

print(f"{average_cost_tonne:.2f}")
print(f"{microbus_relative:.2f}%")
print(f"{lorry_relative:.2f}%")
print(f"{train_relative:.2f}%")
