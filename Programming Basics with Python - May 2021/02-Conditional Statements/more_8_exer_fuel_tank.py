fuel_type = str(input().lower())

fuel_amount_existing = float(input())

if fuel_type == str("diesel"):
    if fuel_amount_existing < 25:
        print(f"Fill your tank with {fuel_type}!")
    else:
        print(f"You have enough {fuel_type}.")


elif fuel_type == str("gasoline"):
    if fuel_amount_existing < 25:
        print(f"Fill your tank with {fuel_type}!")
    else:
        print(f"You have enough {fuel_type}.")

elif fuel_type == str("gas"):
    if fuel_amount_existing < 25:
        print(f"Fill your tank with {fuel_type}!")
    else:
        print(f"You have enough {fuel_type}.")

else:
    print("Invalid fuel!")
