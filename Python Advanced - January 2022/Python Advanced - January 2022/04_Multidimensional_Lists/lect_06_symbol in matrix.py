rows = int(input())
matrix = []
is_found = False

for i in range(rows):
    matrix.append(input())

symbol = input()

for i,row in enumerate(matrix):
    for j, val in enumerate(row):
        if val == symbol:
            print(f"({i}, {j})")
            is_found = True
            break
    if is_found:
        break
if not is_found:
    print(f"{symbol} does not occur in the matrix")
