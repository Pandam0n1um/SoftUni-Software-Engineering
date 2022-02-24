rows, cols = [int(x) for x in input().split()]
size = rows * cols

string = input()
multiplier = 1 + size // len(string)
snake = string * multiplier
for i in range(rows):
    curr_row = snake[i * cols:(i + 1) * cols]
    if i % 2 == 0:
        print(curr_row)
    else:
        print(curr_row[::-1])
