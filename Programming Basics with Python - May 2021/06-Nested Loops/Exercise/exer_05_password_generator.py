value_n = int(input())
value_L = int(input())
i_1 = 1
i_2 = 1
i_3 = 97
i_4 = 97
i_5 = 0
i_3_str=None
i_4_str=None
for i_1 in range(1,value_n):
    for i_2 in range(1,value_n):
        for i_3 in range(97, 97 + value_L):
            i_3_str = chr(i_3)
            for i_4 in range(97, 97 + value_L):
                i_4_str = chr(i_4)
                for i_5 in range(1,value_n+1):
                    if i_1 < i_5 > i_2:
                        print(f"{i_1}{i_2}{i_3_str}{i_4_str}{i_5}", end=' ')