# energy = int(input())
# counter = 0
# is_enough = True
# while True:
#     command = input()
#     if command == "End of battle":
#         break
#     distance = int(command)
#     if energy >= distance:
#         counter += 1
#         energy -= distance
#         if counter % 3 == 0:
#             energy += counter
#     else:
#         is_enough = False
#         break
#
# if is_enough:
#     print(f"Won battles: {counter}. Energy left: {energy}")
#
# else:
#     print(f"Not enough energy! Game ends with {counter} won battles and {energy} energy")

energy = int(input())
battles_won = 0
enough_energy = True

command = input()

while command != "End of battle":
    command_as_int = int(command)

    if energy - command_as_int < 0:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
        enough_energy = False
        break
    battles_won += 1
    energy -= command_as_int
    if battles_won % 3 == 0:
        energy += battles_won
    command = input()

if enough_energy:
    print(f"Won battles: {battles_won}. Energy left: {energy}")