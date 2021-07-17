# age_lily = int(input())
# washing_machine_price = float(input())
# toy_price = int(input())
# money_gathered = 0
# count_toys = 0
# count_money = 0
#
# for num in range(age_lily):
#     if num % 2 == 0:
#         count_toys += 1
#     else:
#         count_money += 10 + 10 * (num - 1) / 2 - 1
#
# money_gathered = count_money + (count_toys * toy_price)
# diff = abs(money_gathered - washing_machine_price)
#
# if money_gathered >= washing_machine_price:
#     print(f"Yes! {diff:.2f}")
# else:
#     print(f"No! {diff:.2f}")

age_lily = int(input())
washing_machine_price = float(input())
toy_price = int(input())
money_gathered = 0
count_toys = 0
count_money = 0
amount=10

for num in range(age_lily):
    if num % 2 == 0:
        count_toys += 1
    else:
        count_money += amount - 1
        amount += 10

money_gathered = count_money + (count_toys * toy_price)
diff = abs(money_gathered - washing_machine_price)

if money_gathered >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")

