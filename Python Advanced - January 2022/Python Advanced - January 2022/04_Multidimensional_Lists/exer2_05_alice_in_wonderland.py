def read_input():
    array = []
    row_size = int(input())
    start_pos = None
    for row in range(row_size):
        current_row = input().split()
        array.append(current_row)
        if "A" in current_row:
            start_pos = (row, current_row.index("A"))
    return array, start_pos


def move(field, start):
    tea_bags = 0
    is_out = False
    curr_pos = start
    moving = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}
    field[start[0]][start[1]] = "*"
    while True:
        direction = input()
        curr_pos = (tuple(map(sum, zip(curr_pos, moving[direction]))))
        if min(curr_pos) < 0 or max(curr_pos) >= len(field):
            is_out = True
            break
        if field[curr_pos[0]][curr_pos[1]] == "R":
            is_out = True
        if field[curr_pos[0]][curr_pos[1]].isnumeric():
            tea_bags += int(field[curr_pos[0]][curr_pos[1]])
        field[curr_pos[0]][curr_pos[1]] = "*"
        if tea_bags>=10:
            is_out=True
            break
        if is_out:
            break
    # sorted_eggs = sorted(eggs_by_direction.items(), key=lambda x: -x[1]['value'])
    # print(eggs_by_direction)
    # print(sorted_eggs[0])
    return field, tea_bags


field, start = read_input()
field, result = move(field, start)
if result >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
for row in field:
    print(*row)
# pprint(start)
# pprint(hole)
