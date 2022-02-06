tot_nom_cost = 0
taxes=0
tot_cost=0
while True:
    command = input()
    if command == "regular" or command=="special":
        taxes= tot_nom_cost * 0.2
        tot_cost=tot_nom_cost+taxes
        if command == "special":
            tot_cost *= 0.9
        break
    price = float(command)
    if price < 0:
        print("Invalid price!")
        continue
    tot_nom_cost += price
if tot_cost <= 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {tot_nom_cost:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {tot_cost:.2f}$")
