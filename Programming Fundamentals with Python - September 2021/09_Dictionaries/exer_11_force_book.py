sides_force = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    force_user = ""
    force_side = ""
    force_change = 0
    force_add = 0
    force_existing = ""
    if " | " in command:
        force_side, force_user = command.split(" | ")
    else:
        force_user, force_side = command.split(" -> ")
        force_change = 1

    if force_side not in sides_force:
        sides_force[force_side] = []

    for side in sides_force:
        if force_user not in sides_force[side]:
            force_add = 1
        else:
            force_add = 0
            force_existing = side
            break

    if force_add == 0 and force_change == 1:
        sides_force[force_existing].remove(force_user)
        sides_force[force_side].append(force_user)

    elif not force_add == 0:
        sides_force[force_side].append(force_user)
    if force_change == 1:
        print(f"{force_user} joins the {force_side} side!")
sorted_sides_force = dict(sorted(sides_force.items(), key=lambda x: (-len(x[1]), x[0])))

for side, side_list in sorted_sides_force.items():
    if len(side_list) > 0:
        print(f"Side: {side}, Members: {len(side_list)}")
        sorted_force_users = sorted(side_list)
        for user in sorted_force_users:
            print(f"! {user}")
#
# import sys
# from io import StringIO
#
# input_1 = """Lighter | Royal
# Darker | DCay
# Ivan Ivanov -> Lighter
# DCay -> Lighter
# Lumpawaroo"""
#
# sys.stdin = StringIO(input_1)
#
# command = input()
#
# stats_dict = {}
#
# while not command == "Lumpawaroo":
#     if "|" in command:
#         command = command.split(" | ")
#         force_side, force_user = command[0], command[1]
#
#         if force_side not in stats_dict.keys() and force_user not in [user for array in stats_dict.values() for user in
#                                                                       array]:
#             stats_dict[force_side] = [force_user]
#         elif force_side in stats_dict.keys() and force_user not in [user for array in stats_dict.values() for user in
#                                                                     array]:
#             stats_dict[force_side].append(force_user)
#     else:
#         command = command.split(" -> ")
#         force_side, force_user = command[1], command[0]
#
#         if force_user in [user for array in stats_dict.values() for user in array]:
#             [values.remove(value) for keys, values in stats_dict.items() for value in values if value == force_user]
#             try:
#                 if stats_dict[force_side]:
#                     stats_dict[force_side].append(force_user)
#             except:
#                 stats_dict.setdefault(force_side, [force_user])
#         elif force_user not in [user for array in stats_dict.values() for user in array]:
#             try:
#                 if stats_dict[force_side]:
#                     stats_dict[force_side].append(force_user)
#             except:
#                 stats_dict.setdefault(force_side, [force_user])
#         elif force_side not in stats_dict.keys() and force_user not in [user for array in stats_dict.values() for user
#                                                                         in array]:
#             stats_dict.setdefault(force_side, [force_user])
#         print(f"{force_user} joins the {force_side} side!")
#
#     command = input()
# else:
#     stats_dict = {keys: values for keys, values in stats_dict.items() if values}
#     for keys, values in sorted(stats_dict.items(), key=lambda x: (-len(x[1]), x[0])):
#         print(f'Side: {keys}, Members: {len(stats_dict[keys])}')
#         [print(f"! {user}") for user in sorted(values, key=lambda x: x[0])]
a = 5
