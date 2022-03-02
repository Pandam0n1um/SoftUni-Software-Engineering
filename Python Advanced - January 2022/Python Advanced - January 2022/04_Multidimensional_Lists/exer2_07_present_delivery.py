# def read_in():
#     initial_gifts = int(input())
#     hood_size = int(input())
#     nice_kids = 0
#     santa_pos = None
#     arr = []
#     for _ in range(hood_size):
#         curr_row = input().split()
#         arr.append(curr_row)
#         if "S" in curr_row:
#             santa_pos = (_, curr_row.index("S"))
#         if "V" in curr_row:
#             nice_kids += curr_row.count("V")
#     return arr, santa_pos, nice_kids, initial_gifts
#
#
# hood, curr_pos, good_kids, gifts = read_in()
# gifted = 0
# nice_kids_gifted = 0
# while True:
#     move = {'up': (-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}
#     command = input()
#     if command == "Christmas morning":
#         break
#     temp_pos = tuple(map(sum, zip(curr_pos, move[command])))
#     if hood[temp_pos[0]][temp_pos[1]] == "V":
#         gifted += 1
#         nice_kids_gifted += 1
#     elif hood[temp_pos[0]][temp_pos[1]] == "C":
#         for house in move.values():
#             check_house = tuple(map(sum, zip(temp_pos, house)))
#             if hood[check_house[0]][check_house[1]] == "V":
#                 gifted += 1
#                 nice_kids_gifted += 1
#             elif hood[check_house[0]][check_house[1]] == "X":
#                 gifted += 1
#             hood[check_house[0]][check_house[1]] = "-"
#             if gifted == gifts:
#                 break
#     hood[curr_pos[0]][curr_pos[1]] = "-"
#     curr_pos = temp_pos
#     hood[curr_pos[0]][curr_pos[1]] = "S"
#     if gifted == gifts:
#         break
# diff = good_kids - nice_kids_gifted
# if nice_kids_gifted < good_kids and gifted == gifts:
#     print("Santa ran out of presents!")
# [print(*row) for row in hood]
# if diff > 0:
#     print(f"No presents for {diff} nice kid/s.")
# else:
#     print(f"Good job, Santa! {good_kids} happy nice kid/s.")
#
def is_valid(r, c, field):
    return 0 <= r < len(field) and 0 <= c < len(field)


def get_next_pos(direction, r, c):
    if direction == "right":
        return r, c + 1
    elif direction == "left":
        return r, c - 1
    elif direction == "up":
        return r - 1, c
    elif direction == "down":
        return r + 1, c


presents_available = int(input())
neighbourhood_size = int(input())
matrix = []
santa_r, santa_c = 0, 0
delivered_to_good_kids = 0
good_kids = 0

for row in range(neighbourhood_size):
    row_data = input().split()
    matrix.append(row_data)
    for col in range(neighbourhood_size):
        if row_data[col] == "S":
            santa_r, santa_c = row, col
        if row_data[col] == "V":
            good_kids += 1

while True:
    line = input()
    if line == "Christmas morning":
        break
    matrix[santa_r][santa_c] = "-"
    previous_r, previous_c = santa_r, santa_c
    santa_r, santa_c = get_next_pos(line, santa_r, santa_c)
    if matrix[santa_r][santa_c] == "V":
        presents_available -= 1
        delivered_to_good_kids += 1
    elif matrix[santa_r][santa_c] == "C":
        counter = 0
        while counter < 4:
            if matrix[santa_r][santa_c - 1] == "V" and presents_available:
                delivered_to_good_kids += 1
                presents_available -= 1
                matrix[santa_r][santa_c - 1] = "-"
            elif matrix[santa_r][santa_c - 1] == "X" and presents_available:
                presents_available -= 1
                matrix[santa_r][santa_c - 1] = "-"
            counter += 1
            if matrix[santa_r][santa_c + 1] == "V" and presents_available:
                delivered_to_good_kids += 1
                presents_available -= 1
                matrix[santa_r][santa_c + 1] = "-"
            elif matrix[santa_r][santa_c + 1] == "X" and presents_available:
                presents_available -= 1
                matrix[santa_r][santa_c + 1] = "-"
            counter += 1
            if matrix[santa_r][santa_c - 1] != matrix[previous_r][previous_c]:
                if matrix[santa_r - 1][santa_c] == "V" and presents_available:
                    delivered_to_good_kids += 1
                    presents_available -= 1
                    matrix[santa_r - 1][santa_c] = "-"
                elif matrix[santa_r - 1][santa_c] == "X" and presents_available:
                    presents_available -= 1
                    matrix[santa_r - 1][santa_c] = "-"
            counter += 1
            if matrix[santa_r][santa_c - 1] != matrix[previous_r][previous_c]:
                if matrix[santa_r + 1][santa_c] == "V" and presents_available:
                    delivered_to_good_kids += 1
                    presents_available -= 1
                    matrix[santa_r + 1][santa_c] = "-"
                elif matrix[santa_r + 1][santa_c] == "X" and presents_available:
                    presents_available -= 1
                    matrix[santa_r + 1][santa_c] = "-"
            counter += 1
    matrix[santa_r][santa_c] = "S"
    if presents_available == 0 or delivered_to_good_kids == good_kids:
        break

if presents_available == 0:
    print("Santa ran out of presents!")
for row in matrix:
    print(*row, sep=" ")
if delivered_to_good_kids == good_kids:
    print(f"Good job, Santa! {delivered_to_good_kids} happy nice kid/s.")
else:
    print(f"No presents for {good_kids - delivered_to_good_kids} nice kid/s.")