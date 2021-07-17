price_puzzle = 2.60

price_doll = 3

price_teddy_bear = 4.10

price_minion = 8.20

price_truck = 2

cost_holiday = float(input())

amount_puzzle = float(input())

amount_doll = float(input())

amount_teddy_bear = float(input())

amount_minion = float(input())

amount_truck = float(input())

total_amount=float(amount_puzzle+amount_doll+amount_teddy_bear+amount_minion+amount_truck)

nominal_price = float(
    price_puzzle * amount_puzzle + price_doll * amount_doll + price_teddy_bear * amount_teddy_bear +
    price_minion * amount_minion + price_truck * amount_truck)

nominal_profit=float(nominal_price*0.9)

discounted_price=float(nominal_price*0.75)

discounted_profit=float(discounted_price*0.9)

# print(nominal_price)
#
# print(nominal_profit)
#
# print(discounted_price)
#
# print(discounted_profit)
#
# print(total_amount)

if total_amount<50 and nominal_profit>=cost_holiday:
    print(f"Yes! {nominal_profit-cost_holiday:.2f} lv left.")

elif total_amount>=50 and discounted_profit>=cost_holiday:
    print(f"Yes! {discounted_profit-cost_holiday:.2f} lv left.")

elif total_amount<50 and nominal_price<cost_holiday:
    required_money=float(cost_holiday-nominal_profit)
    print(f"Not enough money! {required_money:.2f} lv needed.")

elif total_amount>=50 and discounted_profit<cost_holiday:
    required_money=float(cost_holiday-discounted_profit)
    print(f"Not enough money! {required_money:.2f} lv needed.")

