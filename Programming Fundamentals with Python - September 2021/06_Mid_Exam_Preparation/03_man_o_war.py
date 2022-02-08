def fire(indx, dmg):
    warship[indx] -= dmg
    if warship[indx] <= 0:
        print("You won! The enemy ship has sunken.")
        exit()


def defend(start_indx, end_indx, dmg):
    for i in range(start_indx, end_indx + 1):
        pirate_ship[i] -= dmg
    if min(pirate_ship) <= 0:
        print("You lost! The pirate ship has sunken.")
        exit()


def repair(indx, dmg):
    pirate_ship[indx] += dmg
    if pirate_ship[indx] > max_health_cap:
        pirate_ship[indx] = max_health_cap


pirate_ship = [int(i) for i in input().split(">")]
warship = [int(i) for i in input().split(">")]
max_health_cap = int(input())

while True:
    command = input().split()
    action = command[0]
    if action == "Retire":
        break

    if action == "Status":
        to_repair = [i for i in pirate_ship if i < 0.2 * max_health_cap]
        print(f"{len(to_repair)} sections need repair.")
        continue
    first_index = int(command[1])
    second_index = 0
    if 2 < len(command):
        second_index = int(command[2])

    if action == "Fire" and 0 <= first_index < len(warship):
        fire(first_index, second_index)
    elif action == "Defend" and 0 <= first_index < len(pirate_ship) and 0 <= second_index < len(pirate_ship):
        damage = int(command[3])
        defend(first_index, second_index, damage)
    elif action == "Repair" and 0 <= first_index < len(pirate_ship):
        repair(first_index, second_index)

print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(warship)}")
