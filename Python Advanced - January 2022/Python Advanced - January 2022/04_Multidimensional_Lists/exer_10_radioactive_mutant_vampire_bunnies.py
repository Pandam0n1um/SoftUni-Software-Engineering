def read_input():
    row_size, col_size = [int(x) for x in input().split()]
    bunny_lair = []
    start_pos = None
    bunny_pos = []

    for row in range(row_size):
        current_row = list(input())
        bunny_lair.append(current_row)
        for col, val in enumerate(current_row):
            if val == "P":
                start_pos = (row, col)
            if val == "B":
                bunny_pos.append((row, col))
    commands = input()
    return commands, bunny_lair, start_pos, bunny_pos


def move(movement, layout, position, bunny_set):
    lair_rows = len(lair)
    lair_cols = len(lair[0])
    is_free = False
    is_alive = True
    GUIDE = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
    nearest_bunnies = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for el in movement:
        temp_pos = [sum(x) for x in zip(GUIDE[el], position)]
        layout[position[0]][position[1]]='.'
        if not 0 <= temp_pos[0] < lair_rows or not 0 <= temp_pos[1] < lair_cols:
            is_free = True
        else:
            position=temp_pos
            if layout[position[0]][position[1]]=='B':
                is_alive=False
            else:
                layout[position[0]][position[1]]='P'


        temp_set=bunny_set.copy()
        length = len(temp_set)
        for idx in range(length):
            new_bunnies = [tuple(map(sum, zip(x, bunny_set[idx]))) for x in nearest_bunnies]
            for pos_to_inf in new_bunnies:
                if check_pos(pos_to_inf, lair_rows, lair_cols):
                    if layout[pos_to_inf[0]][pos_to_inf[1]] == "P":
                        layout[pos_to_inf[0]][pos_to_inf[1]]='B'
                        is_alive = False
                    elif layout[pos_to_inf[0]][pos_to_inf[1]] == ".":
                        layout[pos_to_inf[0]][pos_to_inf[1]] = "B"
                        bunny_set.append((pos_to_inf[0],pos_to_inf[1]))
                    elif layout[pos_to_inf[0]][pos_to_inf[1]]=='B':
                        continue
        if is_free:
            return is_free, layout, position
        if not is_alive:
            return is_alive, layout, position
        temp_set=bunny_set



def check_pos(cur_bunny_pos, lair_rows, lair_cols):
    if not 0 <= cur_bunny_pos[0] < lair_rows or not 0 <= cur_bunny_pos[1] < lair_cols:
        return False
    return True


directions, lair, start, bunnies = read_input()

endstate,end_lair,end_pos=move(directions, lair, start, bunnies)

for row in end_lair:
    print(''.join(row))

if endstate:
    print(f"won: {end_pos[0]} {end_pos[1]}")
else:
    print(f"dead: {end_pos[0]} {end_pos[1]}")
