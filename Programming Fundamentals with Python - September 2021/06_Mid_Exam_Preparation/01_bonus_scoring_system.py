# import math
#
# number_students = int(input())
# total_lectures = int(input())
# additional_bonus = int(input())
#
# max_bonus = 0
# max_lectures = 0
#
# for student in range(number_students):
#     lectures = int(input())
#     bonus = (lectures / total_lectures * (5 + additional_bonus))
#     if bonus > max_bonus:
#         max_bonus = bonus
#         max_lectures = lectures
#
# print(f"Max Bonus: {math.ceil(max_bonus)}.")
# print(f"The student has attended {max_lectures} lectures.")

import sys

students_count = int(input())
lectures_count = int(input())
add_bonus = int(input())

max_num = -sys.maxsize
atten = 0

for student in range(students_count):
    attendance = int(input())
    total_bonus = (attendance / lectures_count) * (5 + add_bonus)
    if max_num < total_bonus:
        max_num = total_bonus
        atten = attendance

print(f"Max Bonus: {round(max_num)}.")
print(f"The student has attended {atten} lectures.")
