budget = float(input())

ticket_category = str(input())

group_count = int(input())

transportation_cost = None

total_ticket_cost = None

if ticket_category == str("Normal"):
    ticket_price = 249.99
    total_ticket_cost = (ticket_price*group_count)

elif ticket_category == str("VIP"):
    ticket_price = 499.99
    total_ticket_cost = (ticket_price*group_count)

if 1 <= group_count <= 4:
    transportation_cost = (budget * 0.75)
elif 5 <= group_count <= 9:
    transportation_cost = (budget * 0.60)
elif 10 <= group_count <= 24:
    transportation_cost = (budget * 0.50)
elif 25 <= group_count <= 49:
    transportation_cost = (budget * 0.40)
elif 50 <= group_count:
    transportation_cost = (budget * 0.25)

total_expenses=(total_ticket_cost+transportation_cost)
diff=abs(budget-total_expenses)

if total_expenses<=budget:
    print(f"Yes! You have {diff:.2f} leva left.")

else:
    print(f"Not enough money! You need {diff:.2f} leva.")