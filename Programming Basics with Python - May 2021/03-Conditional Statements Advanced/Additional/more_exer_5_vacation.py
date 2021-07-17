budget=float(input())
season=str(input())

residence_type=None
residence_expenses=None
residence_location=None

if budget<=1000:
    residence_type=str("Camp")

    if season==str("Summer"):
        residence_expenses=(budget*0.65)
    elif season==str("Winter"):
        residence_expenses = (budget * 0.45)

elif 1000<budget<=3000:
    residence_type = str("Hut")

    if season==str("Summer"):
        residence_expenses=(budget*0.80)
    elif season==str("Winter"):
        residence_expenses = (budget * 0.60)

elif 3000 < budget:
    residence_type = str("Hotel")
    residence_expenses=(budget*0.9)

if season==str("Summer"):
    residence_location=str("Alaska")
elif season==str("Winter"):
    residence_location = str("Morocco")

print(f"{residence_location} - {residence_type} - {residence_expenses:.2f}")