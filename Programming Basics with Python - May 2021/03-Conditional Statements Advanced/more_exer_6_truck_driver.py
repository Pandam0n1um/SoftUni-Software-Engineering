season = str(input())
distance_month_km = float(input())

cost_km = None

if distance_month_km <= 5000:
    if season==str("Spring") or season==str("Autumn"):
        cost_km=0.75
    elif season==str("Summer"):
        cost_km = 0.90
    elif season==str("Winter"):
        cost_km = 1.05

elif 5000 < distance_month_km <= 10000:

    if season==str("Spring") or season==str("Autumn"):
        cost_km=0.95
    elif season==str("Summer"):
        cost_km = 1.10
    elif season==str("Winter"):
        cost_km = 1.25

elif 10000 < distance_month_km <= 20000:
    cost_km = 1.45

money_earned=(4*(cost_km*distance_month_km)*0.9)

print(f"{money_earned:.2f}")
