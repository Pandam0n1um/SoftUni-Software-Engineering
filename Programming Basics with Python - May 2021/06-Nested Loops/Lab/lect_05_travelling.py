destination=str(input())

money_total=0

while not destination=="End":
    budget=float(input())
    while money_total<budget:
        saving = float(input())
        money_total+=saving
    print(f"Going to {destination}!")
    money_total=0
    destination=str(input())