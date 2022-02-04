n_input = int(input())

for i in range(1, n_input + 1):
    is_special = False
    str_i = str(i)
    sum_n = 0
    for n in range(0, len(str_i)):
        sum_n += int(str_i[n])
    if sum_n == 5 or sum_n == 7 or sum_n == 11:
        is_special = True

    if is_special:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
