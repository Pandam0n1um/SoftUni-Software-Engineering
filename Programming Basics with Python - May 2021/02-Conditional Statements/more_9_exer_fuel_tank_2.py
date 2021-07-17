fuel_type = str(input().lower())

fuel_amount_purchased = float(input())

discount_card_availability = str(input().lower())

price_gasoline = 2.22

price_diesel = 2.33

price_gas = 0.93

total_nominal_cost = 0

total_cost = 0

if fuel_type == str("diesel"):
    total_nominal_cost = (fuel_amount_purchased * price_diesel)
    if discount_card_availability == str("yes"):
        total_nominal_cost = (total_nominal_cost - (fuel_amount_purchased * 0.12))
    else:
        pass

elif fuel_type == str("gasoline"):
    total_nominal_cost = (fuel_amount_purchased * price_gasoline)
    if discount_card_availability == str("yes"):
        total_nominal_cost = (total_nominal_cost - (fuel_amount_purchased * 0.18))

    else:
        pass

elif fuel_type == str("gas"):
    total_nominal_cost = (fuel_amount_purchased * price_gas)
    if discount_card_availability == str("yes"):
        total_nominal_cost = (total_nominal_cost - (fuel_amount_purchased * 0.08))
    else:
        pass

if fuel_amount_purchased < 20:
    total_cost = total_nominal_cost

elif 20 <= fuel_amount_purchased <= 25:
    total_cost = (total_nominal_cost * 0.92)

elif 25 < fuel_amount_purchased:
    total_cost = (total_nominal_cost * 0.90)

print(f"{total_cost:.2f} lv.")
