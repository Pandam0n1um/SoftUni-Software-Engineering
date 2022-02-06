# people_count = int(input())
# lift_list = [int(i) for i in input().split()]
# free_list = []
# is_enough = -1
# for count, wagon in enumerate(lift_list):
#     free_space = 4 - lift_list[count]
#
#     if free_space <= people_count:
#         lift_list[count] += free_space
#         people_count -= free_space
#     else:
#         lift_list[count] += people_count
#         people_count = 0
#     if people_count == 0:
#         is_enough = 0
#         if min(lift_list) < 4:
#             is_enough = 1
#         break
#
# if is_enough == -1:
#     print(f"There isn't enough space! {people_count} people in a queue!")
# elif is_enough == 1:
#     print(f"The lift has empty spots!")
# print(*lift_list)

#++++++++++++++++++++++++++++++++++

# is_wag_enough = False
# for index, item in enumerate(lift_list):
#     free_room = (4 - int(lift_list[index]))
#     if people_count == 0:
#         is_wag_enough = 0
#     elif people_count > 0:
#         lift_list[index] += free_room
#         people_count -= free_room
#         is_wag_enough = 1
#
#     else:
#         is_wag_enough = -1
#
# if is_wag_enough < 0:
#     print(f"There isn't enough space! {people_count} people in a queue!")
# if is_wag_enough == 0:
#     print(f"The lift has empty spots!")
# elif is_wag_enough == 1:
#     print(f"The lift has empty spots!")
# print(*lift_list)

waiting_people = int(input())
lift_state = [int(s) for s in input().split()]
the_lift_has_empty_slots = False
for index in range(len(lift_state)):

    if lift_state[index] == 0 and waiting_people >= 4:
        lift_state[index] += 4
        waiting_people -= 4
    else:
        if lift_state[index] > 0:
            dif = abs(lift_state[index] - 4)
        else:
            dif = waiting_people
            the_lift_has_empty_slots = True
        lift_state[index] += dif
        waiting_people -= dif
if the_lift_has_empty_slots:
    print("The lift has empty spots!")
    print(" ".join(map(str, lift_state)))
else:
    if waiting_people == 0:
        print(" ".join(map(str, lift_state)))
    else:
        print(f"There isn't enough space! {waiting_people} people in a queue!")
        print(" ".join(map(str, lift_state)))