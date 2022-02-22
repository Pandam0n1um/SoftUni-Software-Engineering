rows,columns=[int(el) for el in input().split(', ')]

matrix=[]

for i in range(rows):
    matrix.append([int(el) for el in input().split(', ')])
total=sum([sum(elem) for elem in matrix])
print(total)
print(matrix)
