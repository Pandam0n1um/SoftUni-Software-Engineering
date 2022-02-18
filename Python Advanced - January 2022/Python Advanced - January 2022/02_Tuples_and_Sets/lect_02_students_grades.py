count = int(input())

grades = {}

for _ in range(count):
    student, grade = input().split()
    if student not in grades:
        grades[student] = []
    grades[student].append(float(grade))

for name, value in grades.items():
    avg = sum(value) / len(value)
    grades_string = " ".join(map(lambda grade: f"{grade:.2f}", value))

    print(f"{name} -> {grades_string} (avg: {avg:.2f})")
