rows = int(input())

matrix = []

for i in range(rows):
    matrix.extend([int(el) for el in input().split(', ')])
print(matrix)
