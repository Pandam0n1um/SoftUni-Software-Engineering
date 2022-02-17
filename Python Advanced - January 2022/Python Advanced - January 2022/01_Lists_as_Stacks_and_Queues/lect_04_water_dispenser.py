from collections import deque

people = deque()

quantity = int(input())

while True:
    command = input()
    if command == "Start":
        break
    people.append(command)

while True:
    command = input().split()
    if command[0] == "End":
        break
    qty = int(command[-1])
    if "refill" in command:
        quantity += qty
    elif qty <= quantity:
        quantity -= qty
        print(f"{people.popleft()} got water")
    else:
        print(f"{people.popleft()} must wait")
print(f"{quantity} liters left")
