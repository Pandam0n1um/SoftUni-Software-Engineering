rows = int(input())
matrix = []

sum_diagonal = 0

for i in range(rows):
    curr_row = ([int(el) for el in input().split()])
    sum_diagonal += curr_row[i]
print(sum_diagonal)
