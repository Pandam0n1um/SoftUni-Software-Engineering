from collections import deque

customers = deque([int(x) for x in input().split(', ')])
taxis = [int(x) for x in input().split(', ')]
time_passed = 0
while True:
    if not (customers and taxis):
        break
    curr_taxi = taxis.pop()
    curr_cust = customers.popleft()
    if curr_taxi < curr_cust:
        customers.appendleft(curr_cust)
    else:
        time_passed += curr_cust

if not customers:
    print(f"All customers were driven to their destinations\nTotal time: {time_passed} minutes")
else:
    print(
        f"Not all customers were driven to their destinations\nCustomers left: {', '.join(str(cust) for cust in customers)}")
