number_N=int(input())

for number_1 in range(1,10):
    for number_2 in range(1,10):
        sum_1_2=number_1+number_2
        for number_3 in range(1,10):
            for number_4 in range(1,10):
                sum_3_4=number_3+number_4
                if sum_1_2==sum_3_4 and number_N%sum_1_2==0:
                    print(f"{number_1}{number_2}{number_3}{number_4}", end=" ")