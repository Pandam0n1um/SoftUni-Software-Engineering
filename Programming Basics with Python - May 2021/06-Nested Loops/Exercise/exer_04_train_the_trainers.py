number_members = int(input())
sum_marks_total = 0
total_marks_counter = 0
while True:
    input_command = input()
    if input_command == "Finish":
        break

    presentation_title = str(input_command)
    sum_marks_presentation = 0
    total_marks_counter += number_members

    for i in range(0,number_members):
        current_mark = float(input())
        sum_marks_presentation += current_mark
        sum_marks_total += current_mark

    average_mark_presentation = sum_marks_presentation / number_members
    print(f"{presentation_title} - {average_mark_presentation:.2f}.")

average_mark_total = sum_marks_total / total_marks_counter
print(f"Student's final assessment is {average_mark_total:.2f}.")
