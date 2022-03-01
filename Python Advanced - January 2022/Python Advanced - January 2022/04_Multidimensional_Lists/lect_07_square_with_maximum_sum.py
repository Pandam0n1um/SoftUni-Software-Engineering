rows, columns = [int(el) for el in input().split(', ')]

matrix = []

for i in range(rows):
    matrix.append([int(el) for el in input().split(', ')])

sum_max_matrix = 0
max_matrix = []

for i in range(rows - 1):
    for j in range(columns - 1):
        current_matrix = [matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1]]
        if sum(current_matrix) > sum_max_matrix:
            sum_max_matrix = sum(current_matrix)
            max_matrix = current_matrix

print(f"{max_matrix[0]} {max_matrix[1]}\n{max_matrix[2]} {max_matrix[3]}")
print(sum_max_matrix)
