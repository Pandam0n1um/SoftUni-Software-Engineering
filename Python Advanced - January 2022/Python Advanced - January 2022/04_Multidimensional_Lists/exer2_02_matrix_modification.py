from pprint import pprint


def operation(array, pos,add_sub):
    if add_sub=="Add":
        array[pos[0]][pos[1]]+=pos[2]
    else:
        array[pos[0]][pos[1]]-= pos[2]
    return array


rows = int(input())
matrix = [[int(j) for j in input().split()] for i in range(rows)]

while True:
    command = input()
    if command == "END":
        break
    action, *tokens = command.split()
    tokens = [int(x) for x in tokens]
    if not (0 <= tokens[0] < rows) or not (0 <= tokens[1] <= rows):
        print("Invalid coordinates")
    else:
        matrix = operation(matrix, tokens, action)
[print(*row) for row in matrix]
