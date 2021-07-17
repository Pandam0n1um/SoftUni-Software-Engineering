budget = float(input())

season = str(input())

destination = None
resort_type = None
expenses = None

if budget <= 100:
    destination = str("Bulgaria")
    if season == str("summer"):
        resort_type=str("Camp")
        expenses = (budget * 0.3)
    elif season == str("winter"):
        resort_type = str("Hotel")
        expenses = (budget * 0.7)

elif 100 < budget <= 1000:
    destination = str("Balkans")
    if season == str("summer"):
        resort_type = str("Camp")
        expenses = (budget * 0.4)
    elif season == str("winter"):
        resort_type = str("Hotel")
        expenses = (budget * 0.8)

elif 1000 < budget:
    destination = str("Europe")
    resort_type = str("Hotel")
    expenses = (budget * 0.9)

print(f"Somewhere in {destination}")
print(f"{resort_type} - {expenses:.2f}")