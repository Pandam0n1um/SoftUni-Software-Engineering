matrix_size = int(input())

matrix = [[int(j) for j in input().split(', ')] for i in range(matrix_size)]
main_diagonal = []
secondary_diagonal = []

for i in range(matrix_size):
    main_diagonal.append(matrix[i][i])
for j in range(matrix_size):
    secondary_diagonal.append(matrix[j][-j - 1])
sum_primary = sum(main_diagonal)
sum_secondary = sum(secondary_diagonal)
diff = abs(sum_primary - sum_secondary)
# print(main_diagonal)
print(f"Primary diagonal: {', '.join([str(x) for x in main_diagonal])}. Sum: {sum_primary}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum_secondary}")
# print(diff)
