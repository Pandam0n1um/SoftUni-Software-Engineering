from collections import deque


def make_pizza(order, capacity):
    leftover = 0
    completed = order
    if capacity < 0:
        capacity = 0
    if order > capacity:
        leftover = order - capacity
        completed = capacity
    return leftover, completed


pizza_orders = deque([int(x) for x in input().split(', ')])
empl_capacity = [int(x) for x in input().split(', ')]

total = 0

while True:
    if not (pizza_orders and empl_capacity):
        break
    curr_pizza = pizza_orders.popleft()
    curr_empl = empl_capacity.pop()
    while True:
        if (curr_pizza > 10 or curr_pizza <= 0) and pizza_orders:
            curr_pizza = pizza_orders.popleft()
        elif 0 < curr_pizza <= 10:
            break
        elif not pizza_orders:
            empl_capacity.append(curr_empl)
            break

    remainder, compl = make_pizza(curr_pizza, curr_empl)
    total += compl
    if remainder > 0:
        pizza_orders.appendleft(remainder)

if not pizza_orders:
    print(f"All orders are successfully completed!\nTotal pizzas made: {max(0, total)}\nEmployees: ", end="")
    print(*empl_capacity, sep=", ")
else:
    print(f"Not all orders are completed.\nOrders left: ", end="")
    print(*pizza_orders, sep=", ")




# from collections import deque
 
# pizza_orders = deque(int(x) for x in input().split(', '))
# employees = deque(int(x) for x in input().split(', '))
 
# total_pizzas = 0
# while pizza_orders and employees:
    # order = pizza_orders.popleft()
    # employee = employees.pop()
 
    # if order <= 0 or order > 10:
        # employees.append(employee)
        # continue
 
    # total_pizzas += min(employee, order)
 
    # if order > employee:
        # order -= employee
        # pizza_orders.appendleft(order)
 
# if pizza_orders:
    # print("Not all orders are completed.")
    # print(f"Orders left: {', '.join(str(el) for el in pizza_orders)}")
# else:
    # print("All orders are successfully completed!")
    # print(f"Total pizzas made: {total_pizzas}")
    # print(f"Employees: {', '.join(str(el) for el in employees)}")
 