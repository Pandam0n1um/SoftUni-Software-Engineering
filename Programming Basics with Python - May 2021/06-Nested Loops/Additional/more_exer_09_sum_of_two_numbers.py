interval_start = int(input())
interval_end = int(input())
magic_number = int(input())
is_found = False
counter_combinations = 0
sum_numbers = 0

for number_1 in range(interval_start, interval_end + 1):
    for number_2 in range(interval_start, interval_end + 1):
        counter_combinations += 1
        sum_numbers = number_1 + number_2
        if sum_numbers == magic_number:
            is_found = True
            break
    if is_found:
        break
if is_found:
    print(f"Combination N:{counter_combinations} ({number_1} + {number_2} = {magic_number})")
else:
    print(f"{counter_combinations} combinations - neither equals {magic_number}")
