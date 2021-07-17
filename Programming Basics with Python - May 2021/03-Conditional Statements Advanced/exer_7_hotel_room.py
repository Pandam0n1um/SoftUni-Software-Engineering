month = str(input())

amount_nights = int(input())

studio_cost = None
apartment_cost = None

if month == str("May") or month == str("October"):
    studio_cost = 50
    apartment_cost = 65
    if 7 < amount_nights <= 14:
        studio_cost = (studio_cost * 0.95)

    elif amount_nights > 14:
        studio_cost = (studio_cost * 0.7)
        apartment_cost = (apartment_cost * 0.9)

elif month == str("June") or month == str("September"):
    studio_cost = 75.20
    apartment_cost = 68.70
    if amount_nights > 14:
        studio_cost = (studio_cost * 0.8)
        apartment_cost = (apartment_cost * 0.9)


elif month == str("July") or month == str("August"):
    studio_cost = 76
    apartment_cost = 77
    if amount_nights > 14:
        apartment_cost = (apartment_cost * 0.9)


apartment_cost_total = (apartment_cost * amount_nights)
studio_cost_total = (studio_cost * amount_nights)

print(f"Apartment: {apartment_cost_total:.2f} lv.")
print(f"Studio: {studio_cost_total:.2f} lv.")
