range_start = int(input())
range_end = int(input())

for number_1 in range(range_start, range_end + 1):
    is_number_1_even = False
    if number_1 % 2 == 0:
        is_number_1_even = True
    for number_2 in range(range_start, range_end + 1):
        for number_3 in range(range_start, range_end + 1):
            sum_2_3 = number_2 + number_3
            if sum_2_3 % 2 == 1:
                continue
            for number_4 in range(range_start, range_end + 1):
                is_number_4_even = False
                if number_4 % 2==0:
                    is_number_4_even = True
                if (is_number_4_even and is_number_1_even) or (not is_number_1_even and not is_number_4_even)or number_1<number_4:
                    continue
                print(f"{number_1}{number_2}{number_3}{number_4}", end=" ")
