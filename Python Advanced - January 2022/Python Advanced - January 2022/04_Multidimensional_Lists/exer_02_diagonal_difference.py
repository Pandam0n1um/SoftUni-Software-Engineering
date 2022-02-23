matrix_size=int(input())

matrix= [[int(j) for j in input().split()] for i in range(matrix_size)]
main_diagonal=0
secondary_diagonal=0

for i in range(matrix_size):
    main_diagonal+=matrix[i][i]
for j in range(matrix_size):
    secondary_diagonal+=matrix[j][-j-1]
diff=abs(main_diagonal-secondary_diagonal)
# print(main_diagonal)
# print(secondary_diagonal)
print(diff)