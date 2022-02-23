rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for i in range(rows)]

while True:
    command = input()
    if command == "END":
        break
    if not "swap" in command:
        print("Invalid input!")
        continue
    action, *tokens = command.split()
    if not len(tokens)==4:
        print('Invalid input!')
        continue
    tokens = [int(el) for el in tokens]
    if min(tokens) < 0 or max(tokens[0::2]) > rows or max(tokens[1::2]) > cols:
        print("Invalid input!")
        continue
    matrix[tokens[0]][tokens[1]], matrix[tokens[2]][tokens[3]] = matrix[tokens[2]][tokens[3]], matrix[tokens[0]][
        tokens[1]]
    for row in matrix:
        print(*row)
