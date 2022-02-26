def read_input():
    array = []
    row_size = int(input())
    start_pos = None
    for row in range(row_size):
        current_row = input().split()
        array.append(current_row)
        if "B" in current_row:
            start_pos = (row, current_row.index("B"))
    return array, start_pos


def move(field, start):
    eggs_by_direction = {'right': {'value': float('-inf'), 'positions': []},
                         'left': {'value': float('-inf'), 'positions': []},
                         'up': {'value': float('-inf'), 'positions': []},
                         'down': {'value': float('-inf'), 'positions': []}}
    moving = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}
    for direction, increment in moving.items():
        curr_pos = start
        while True:
            curr_pos = (tuple(map(sum, zip(curr_pos, moving[direction]))))
            if min(curr_pos) < 0 or max(curr_pos) >= len(field):
                break
            if field[curr_pos[0]][curr_pos[1]] == "X":
                break
            eggs_by_direction[direction]['value'] += int(field[curr_pos[0]][curr_pos[1]])
            eggs_by_direction[direction]['positions'].append(curr_pos)
    sorted_eggs = sorted(eggs_by_direction.items(), key=lambda x: -x[1]['value'])
    # print(eggs_by_direction)
    # print(sorted_eggs[0])
    return sorted_eggs[0]


field, start = read_input()

best_direction = move(field, start)
if len(best_direction[1]) > 0:
    print(best_direction[0])
    for egg in best_direction[1]['positions']:
        print(f"[{egg[0]}, {egg[1]}]")
    print(best_direction[1]['value'])

# pprint(field)
# print(start)
