rows, cols = [int(x) for x in input().split()]

for i in range(rows):
    curr_row = []
    for j in range(cols):
        char = chr(97 + i) + chr(97 + i + j) + chr(97 + i)
        curr_row.append(char)

    print(*curr_row)
