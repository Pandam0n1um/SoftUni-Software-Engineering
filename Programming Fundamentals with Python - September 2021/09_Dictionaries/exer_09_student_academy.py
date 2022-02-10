number_rows = int(input())
students_dict = {}

for student in range(number_rows):
    student_name = input()
    student_grade = float(input())
    if student_name not in students_dict:
        students_dict[student_name] = []
    students_dict[student_name].append(student_grade)

filtered_students = {}
for student, grades in students_dict.items():
    average = sum(grades) / len(grades)
    if average >= 4.5:
        filtered_students[student] = average
sorted_students = (sorted(filtered_students.items(), key=lambda kvp: (-kvp[1])))

for student,grade in sorted_students:
    print(f"{student} -> {grade:.2f}")
#
# arhivs = {}
#
# for i in range(int(input())):
#     studet = input()
#     grade = float(input())
#
#     if studet not in arhivs:
#         arhivs[studet] = []
#
#     arhivs[studet].append(grade)
#
# f = lambda x: sum(x[1]) / len(x[1]) >= 4.50
# l = list(filter(f, arhivs.items()))
# arhivs = dict(l)
#
# fun = lambda x: sum(x[1]) / len(x[1])
# l_ = sorted(arhivs.items(), key=fun, reverse=True)
# arhivs = dict(l_)
#
# [print(f"{k} -> {sum(v) / len(v):.2f}") for k, v in arhivs.items()]