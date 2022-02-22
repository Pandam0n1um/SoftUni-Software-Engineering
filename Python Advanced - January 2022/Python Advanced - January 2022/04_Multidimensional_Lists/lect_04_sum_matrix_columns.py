rows, columns = [int(el) for el in input().split(', ')]

matrix = []
matrix_sum_col = [0]*columns
for i in range(rows):
    current_row = [int(el) for el in input().split()]
    for idx, val in enumerate(current_row):
        matrix_sum_col[idx] += val

print(*matrix_sum_col,sep='\n')
