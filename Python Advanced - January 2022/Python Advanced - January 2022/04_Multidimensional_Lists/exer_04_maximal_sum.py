import sys

rows, cols = [int(x) for x in input().split()]
max_value = -sys.maxsize
list_max =None
matrix = [[int(j) for j in input().split()] for i in range(rows)]

for i in range(rows - 2):
    for j in range(cols - 2):
        curr_matrix = matrix[i][j:j + 3] + matrix[i + 1][j:j + 3] + matrix[i +2][j:j + 3]
        if sum(curr_matrix) > max_value:
            max_value = sum(curr_matrix)
            list_max =curr_matrix

print(f"Sum = {max_value}")
for i in range(0,9,3):
    print(f"{list_max[i]} {list_max[i+1]} {list_max[i+2]}")

()(((((((((((())))))))))))