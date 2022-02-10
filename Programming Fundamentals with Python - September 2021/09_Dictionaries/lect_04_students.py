courses = {}
searched_course = ""
while True:
    command = input()
    if ":" not in command:
        searched_course = command
        break
    student_name, student_id, course_name = command.split(":")
    if course_name not in courses:
        courses[course_name] = {}
    courses[course_name][student_id] = student_name

searched_course = searched_course.replace("_", " ")
# print(searched_course)

for stud_id, stud_name in courses[searched_course].items():
    print(f"{stud_name} - {stud_id}")
