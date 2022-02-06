def strike(row_n, col_n, is_destroyed=False):
    if ship_array[row_n][col_n] > 0:
        ship_array[row_n][col_n] -= 1
        if ship_array[row_n][col_n] == 0:
            is_destroyed = True
    return is_destroyed


ship_rows_count = int(input())
ship_array = []
ships_destroyed = 0
for rows in range(ship_rows_count):
    current_row = [int(i) for i in input().split()]
    ship_array.append(current_row)
attack_array = input().split()
for attack in attack_array:
    location = attack.split("-")
    row = int(location[0])
    col = int(location[1])
    destroyed = strike(row, col)
    if destroyed:
        ships_destroyed += 1

print(ships_destroyed)
