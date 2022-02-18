from collections import deque

cups = deque([int(el) for el in input().split()])
bottles = deque([int(el) for el in input().split()])

wasted_liters = 0

while True:
    if not (cups and bottles):
        break
    current_bottle = bottles.pop()
    current_cup = cups.popleft()
    diff = current_cup - current_bottle
    if diff > 0:
        current_cup -= current_bottle
        cups.appendleft(current_cup)
    elif diff < 0:
        wasted_liters += abs(diff)

if cups:
    cups = [str(x) for x in list(cups)]
    cups_print = " ".join(cups)
    print(f"Cups: {cups_print}")
else:
    bottles = list(reversed(bottles))
    bottles = [str(x) for x in bottles]
    bottle_print = " ".join(bottles)
    print(f"Bottles: {bottle_print}")
print(f"Wasted litters of water: {wasted_liters}")
