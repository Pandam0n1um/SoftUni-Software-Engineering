floor_count = int(input())
room_per_floor_count = int(input())
floor_value = None

for floor in range(floor_count, 0, -1):
    if floor == floor_count:
        floor_value = str("L")
    elif floor % 2 == 0:
        floor_value = str("O")
    elif not floor % 2 == 0:
        floor_value = str("A")
    for room in range(0, room_per_floor_count):
        print(f"{floor_value}{floor}{room} ", end='')
    print()

#
# floor_count=int(input())
# room_per_floor_count=int(input())
#
# for floor in range(floor_count,0,-1):
#     if floor == floor_count:
#         floor_value=str("L")
#     elif (not floor==floor_count) and floor % 2 == 0:
#         floor_value=str("O")
#     elif not(floor==floor_count and floor % 2 == 0):
#         floor_value=str("A")
#     for room in range(0,room_per_floor_count):
#             print(f"{floor_value}{floor}{room} ", end='')
#     print()
