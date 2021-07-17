import math

count_magnolias = int(input())

count_hyacinth = int(input())

count_roses = int(input())

count_cacti = int(input())

price_present = float(input())

cost_magnolias_total = float(count_magnolias * 3.25)

cost_hyacinth_total = float(count_hyacinth * 4)

cost_roses_total = float(count_roses * 3.5)

cost_cacti_total = float(count_cacti * 8)

cost_total=float(cost_magnolias_total+cost_hyacinth_total+cost_roses_total+
                 cost_cacti_total)

profit_total=float(cost_total*.95)

if price_present<=profit_total:
    amount_money_left=math.floor(profit_total-price_present)
    print(f"She is left with {amount_money_left} leva.")

else:
    amount_money_needed=math.ceil(price_present-profit_total)
    print(f"She will have to borrow {amount_money_needed} leva.")