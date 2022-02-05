is_left_winner = True

times_list = input().split()

times_list = [int(i) for i in times_list]

middle_index = int((len(times_list) - 1) / 2)

left_list = times_list[:middle_index]
right_list = times_list[:middle_index:-1]

result_left = 0
result_right = 0

for steptime in range(len(left_list)):
    current_value = left_list[steptime]
    result_left += current_value
    if current_value == 0:
        result_left *= 0.8

for steptime in range(len(right_list)):
    current_value = right_list[steptime]
    result_right += current_value
    if current_value == 0:
        result_right *= 0.8

if result_left > result_right:
    is_left_winner = False

if is_left_winner:
    print(f"The winner is left with total time: {result_left:.1f}")
else:
    print(f"The winner is right with total time: {result_right:.1f}")
