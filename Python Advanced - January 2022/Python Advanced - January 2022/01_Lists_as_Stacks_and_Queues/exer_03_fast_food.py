from collections import deque

food_qty = int(input())

order_qty = deque([int(x) for x in input().split()])

print(max(order_qty))

while order_qty:
    current = order_qty.popleft()
    if current <= food_qty:
        food_qty -= current
    else:
        print(f"Orders left: {current}", end="")
        while order_qty:
            print(f" {order_qty.popleft()}", end="")
        exit()
print("Orders complete")
