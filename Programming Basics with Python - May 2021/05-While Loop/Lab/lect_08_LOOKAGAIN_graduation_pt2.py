# student_name = str(input())
#
# yearly_mark = float(input())
#
# grade_counter = 1
# sum_grades = 0
#
# while grade_counter <= 12:
#     if yearly_mark < 4:
#         yearly_mark = float(input())
#         if yearly_mark < 4:
#             print(f"{student_name} has been excluded at {grade_counter} grade")
#             break
#
#     sum_grades += yearly_mark
#     if grade_counter==12:
#         break
#     grade_counter += 1
#     yearly_mark = float(input())
#
# average_grade = sum_grades / grade_counter
#
# print(f"{student_name} graduated. Average grade: {average_grade:.2f}")


# name = str(input())
#
# class_number = 0
# bad_grade_counter = 0
# grades_sum = 0
#
# while bad_grade_counter < 2:
#     class_number += 1
#     grade = float(input())
#     grades_sum += grade
#
#     if grade < 4:
#         bad_grade_counter += 1
#         class_number -= 1
#
#     if class_number == 12:
#         break
#
# if bad_grade_counter != 2:
#     average_grade = grades_sum / class_number
#     print(f"{name} graduated. Average grade: {average_grade:.2f}")
#
# else:
#     print(f"{name} has been excluded at {class_number + 1} grade")



student_name = str(input())

grade_counter = 1
sum_grades = 0
bad_grade_count=0
yearly_mark = float(input())

while grade_counter <= 12:
    if yearly_mark < 4:
        bad_grade_count +=1
        if bad_grade_count > 1:
            print(f"{student_name} has been excluded at {grade_counter} grade")
            break
        yearly_mark = float(input())
        continue
    sum_grades += yearly_mark
    bad_grade_count=0
    if grade_counter == 12:
        break
    grade_counter += 1
    yearly_mark = float(input())
average_grade = sum_grades / grade_counter
if bad_grade_count<2:
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")


# student_name = str(input())
#
# grade_counter = 1
# sum_grades = 0
# bad_grade_count=0
# yearly_mark = float(input())
#
# while grade_counter <= 12:
#     if yearly_mark < 4:
#         bad_grade_count +=1
#         if bad_grade_count > 1:
#             print(f"{student_name} has been excluded at {grade_counter} grade")
#             break
#         continue
#     sum_grades += yearly_mark
#     if grade_counter == 12:
#         break
#     grade_counter += 1
#     yearly_mark = float(input())
# average_grade = sum_grades / grade_counter
# if bad_grade_count<2:
#     print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
