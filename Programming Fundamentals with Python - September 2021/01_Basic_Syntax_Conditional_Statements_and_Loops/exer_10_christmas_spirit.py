quantity = int(input())

days = int(input())

ornaments_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15

christmas_spirit = 0
budget = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        christmas_spirit += 5
        budget += quantity * 2
    if day % 3 == 0:
        christmas_spirit += 13
        budget += quantity * 8
    if day % 5 == 0:
        christmas_spirit += 17
        budget += quantity * 15
    if day % 3 == 0 and day % 5 == 0:
        christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        budget += 23
    if day % 10 == 0 and day == days:
        christmas_spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {christmas_spirit}")
