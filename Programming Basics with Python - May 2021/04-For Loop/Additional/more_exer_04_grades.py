students_amount=int(input())
counter_top=0
counter_4_to_5=0
counter_3_to_4=0
counter_fail=0
grade_sum=0

for students in range (students_amount):
    grade_input=float(input())
    if 5<=grade_input:
        counter_top+=1
    elif 4<=grade_input:
        counter_4_to_5+=1
    elif 3<=grade_input:
        counter_3_to_4+=1
    else:
        counter_fail+=1
    grade_sum+=grade_input

percentage_top=(counter_top/students_amount)*100
percentage_4_to_5=(counter_4_to_5/students_amount)*100
percentage_3_to_4=(counter_3_to_4/students_amount)*100
percentage_fail=(counter_fail/students_amount)*100
average_grade=grade_sum/students_amount

print(f"Top students: {percentage_top:.2f}%")
print(f"Between 4.00 and 4.99: {percentage_4_to_5:.2f}%")
print(f"Between 3.00 and 3.99: {percentage_3_to_4:.2f}%")
print(f"Fail: {percentage_fail:.2f}%")
print(f"Average: {average_grade:.2f}")