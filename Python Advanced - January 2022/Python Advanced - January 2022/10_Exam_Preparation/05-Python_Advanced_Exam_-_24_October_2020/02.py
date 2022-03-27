def read_input():
    board = []
    king_pos = []
    queen_loc = []
    for i in range(BOARD_SIZE):
        row = input().split()
        board.append(row)
        for idx, val in enumerate(row):
            if val == 'Q':
                queen_loc.append([i, idx])
            elif val == 'K':
                king_pos = [i, idx]
    return board, king_pos, queen_loc


def scanning(arr, king, queens):
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

    killer_queens = []
    for delta in directions:
        curr_row = king_pos[0]
        curr_col = king_pos[1]
        while True:
            curr_row += delta[0]
            curr_col += delta[1]
            if min(curr_row, curr_col) < 0 or max(curr_row, curr_col) >= BOARD_SIZE:
                break
            if arr[curr_row][curr_col] == 'Q':
                killer_queens.append([curr_row, curr_col])
                break

    return killer_queens


BOARD_SIZE = 8
is_king_safe = True

board, king_pos, queen_loc = read_input()
killer_queens = scanning(board, king_pos, queen_loc)

if killer_queens:
    print(*killer_queens, sep='\n')
else:
    print('The king is safe!')


