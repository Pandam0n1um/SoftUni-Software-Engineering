first_line = input().split()
second_line = input().split()
third_line = input().split()
is_winner = False
is_one = True

first_line_set = set(first_line)
second_line_set = set(second_line)
third_line_set = set(third_line)

import pyf

# if len(first_line_set) == 1 and (not first_line[2]=="0"):
#     is_winner = True
#     if is_winner and first_line[2] == "2":
#         is_one = False
#
# elif len(second_line_set) == 1 and not second_line[2]=="0":
#     is_winner = True
#     if is_winner and second_line[2] == "2":
#         is_one = False
#
# elif len(third_line_set) == 1 and not third_line[2]=="0":
#     is_winner = True
#     if is_winner and third_line[2] == "2":
#         is_one = False
#
# elif first_line[0] == second_line[1] and first_line[0] == third_line[2] and not first_line[0]=="0":
#     is_winner = True
#
# elif first_line[2] == second_line[1] and first_line[2] == third_line[0] and not first_line[2]=="0":
#     is_winner = True
#     if is_winner and first_line[2] == "2":
#         is_one = False
# else:
#     for i in range(len(first_line)):
#         if first_line[i] == second_line[i] and first_line[i] == third_line[i] and not first_line[i]=="0":
#             is_winner = True
#         if is_winner and first_line[i] == "2":
#             is_one = False

if is_winner and is_one:
    print("First player won")
elif is_winner and not is_one:
    print("Second player won")
else:
    print("Draw!")
