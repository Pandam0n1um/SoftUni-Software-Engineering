from pprint import pprint


def read_input():
    field_size = int(input())
    game_field = []
    start_pos = None
    coal = 0
    commands = input().split()
    for row in range(field_size):
        current_row = input().split()
        game_field.append(current_row)
        if "s" in current_row:
            start_col = current_row.index("s")
            start_pos = (row, start_col)
        if "c" in current_row:
            coal += current_row.count("c")
    return commands, game_field, start_pos, coal


directions, field, start, total_coal = read_input()


def move(directions, field, start,total_coals):
    is_over = False
    start_pos = field[start[0]][start[1]]
    current_pos = [start[0], start[1]]
    gathered_coal = 0
    commands = {'up': [-1, 0], 'down': [1, 0], 'right': [0, 1], 'left': [0, -1]}
    for action in directions:
        temp_pos = [sum(x) for x in zip(commands[action], current_pos)]
        if min(temp_pos) >= 0 and max(temp_pos) < len(field):
            current_pos = temp_pos
            current_row, current_col = current_pos
            if field[current_row][current_col] == "c":
                gathered_coal += 1
                field[current_row][current_col]="*"
                if gathered_coal==total_coals:
                    break
            elif field[current_row][current_col] == "e":
                is_over = True
                break

    return gathered_coal, current_pos, is_over


gathered_coal, final_pos, finished = move(directions, field, start,total_coal)


if finished:
    print(f"Game over! ({final_pos[0]}, {final_pos[1]})")
elif gathered_coal==total_coal:
    print(f"You collected all coal! ({final_pos[0]}, {final_pos[1]})")
else:
    print(f"{total_coal-gathered_coal} pieces of coal left. ({final_pos[0]}, {final_pos[1]})")

# pprint(field)

# print(start)
# print(total_coal)
