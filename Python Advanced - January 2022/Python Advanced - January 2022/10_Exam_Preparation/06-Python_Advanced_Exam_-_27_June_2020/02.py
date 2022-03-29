def evaluate_field(row, col):
    directions = [
        [-1, 0],
        [-1, 1],
        [0, 1],
        [1, 1],
        [1, 0],
        [1, -1],
        [0, -1],
        [-1, -1],
    ]
    total = 0
    for cell in directions:
        checked_row = row + cell[0]
        checked_col = col + cell[1]
        if is_inside(checked_row, checked_col):
            if field[checked_row][checked_col] == '*':
                total += 1
    return total


def is_inside(checked_row, checked_col):
    if 0 <= min(checked_row, checked_col) and SIZE > max(checked_row, checked_col):
        return True


SIZE = int(input())
mines_count = int(input())
field = [['x' for col in range(SIZE)] for row in range(SIZE)]

for n in range(mines_count):
    curr_cell = input().split(', ')
    curr_row = int(curr_cell[0][1:])
    curr_col = int(curr_cell[1][:-1])
    field[curr_row][curr_col] = '*'

for i in range(SIZE):
    curr_row = field[i]
    for j, val in enumerate(curr_row):
        if not val == "*":
            curr_row = i
            curr_col = j
            value = evaluate_field(curr_row, curr_col)
            field[curr_row][curr_col] = value

for row in field:
    print(*row, sep=' ')
