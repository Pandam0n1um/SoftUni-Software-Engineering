import re

pattern=r"^%(?P<name>[A-Z][a-z]+)%.*<(?P<product>\w+)>.*\|(?P<qty>\d+)\|\D*(?P<price>\d+(\.\d+)?)\$$"
customers={}
total_income=0
while True:
    command=input()
    if command=="end of shift":
        break
    valid_order=re.search(pattern,command)
    if valid_order:
        curr_order=valid_order.groupdict()
        total_cost=int(curr_order['qty'])*float(curr_order['price'])
        print(f"{curr_order['name']}: {curr_order['product']} - {total_cost:.2f}")
        total_income+=total_cost

print(f"Total income: {total_income:.2f}")