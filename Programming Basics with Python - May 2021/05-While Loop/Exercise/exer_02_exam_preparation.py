poor_grades_limit = int(input())

problem_count = 0
grades_sum = 0
poor_grades_counter = 0
last_problem_name = None
has_failed = True

while poor_grades_counter < poor_grades_limit:
    problem_name = str(input())
    if problem_name == "Enough":
        has_failed = False
        break

    grades_value = int(input())
    problem_count += 1
    if grades_value <= 4:
        poor_grades_counter += 1
    grades_sum += grades_value
    last_problem_name = problem_name

if has_failed:
    print(f"You need a break, {poor_grades_limit} poor grades.")
else:
    average_grade_value = grades_sum / problem_count
    print(f"Average score: {average_grade_value:.2f}")
    print(f"Number of problems: {problem_count}")
    print(f"Last problem: {last_problem_name}")
