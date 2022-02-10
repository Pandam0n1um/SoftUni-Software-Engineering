course_dict = {}
while True:
    command = input()
    if command == "end":
        break
    course, students = command.split(" : ")

    if course not in course_dict:
        course_dict[course] = []
    course_dict[course].append(students)

for course in course_dict:
    course_dict[course] = sorted(course_dict[course])

course_dict_sorted = dict(sorted(course_dict.items(), key=lambda x: len(x[1]),reverse=True))

for key,value in course_dict_sorted.items():
    print(f"{key}: {len(value)}")

    for student in value:
        print(f"-- {student}")
