budget = float(input())

season = str(input())

travel_class = None
travel_expenses = None
car_type = None

if budget <= 100:
    travel_class = str("Economy class")
    if season == str("Summer"):
        car_type = str("Cabrio")
        travel_expenses=(budget*0.35)
    elif season == str("Winter"):
        car_type = str("Jeep")
        travel_expenses = (budget * 0.65)

elif 100 < budget <= 500:
    travel_class = str("Compact class")
    if season == str("Summer"):
        car_type = str("Cabrio")
        travel_expenses=(budget*0.45)
    elif season == str("Winter"):
        car_type = str("Jeep")
        travel_expenses = (budget * 0.80)
elif 500 < budget:
    travel_class = str("Luxury class")
    car_type = str("Jeep")
    travel_expenses = (budget * 0.90)

print(f"{travel_class}")

print(f"{car_type} - {travel_expenses:.2f}")