value_N = int(input())

for i_1 in range(1,10):
    is_1_special = False
    if (value_N % i_1) == 0:
        is_1_special = True
    for i_2 in range(1,10):
        is_2_special = False
        if (value_N % i_2 )== 0:
            is_2_special = True
        for i_3 in range(1,10):
            is_3_special = False
            if (value_N % i_3)== 0:
                is_3_special = True
            for i_4 in range(1,10):
                is_4_special = False
                if (value_N % i_4) == 0:
                    is_4_special = True
                if is_1_special and is_2_special and is_3_special and is_4_special:
                    print(f"{i_1}{i_2}{i_3}{i_4}", end=" ")