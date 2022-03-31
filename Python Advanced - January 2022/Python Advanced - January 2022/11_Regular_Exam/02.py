def read_matrix(FIELD_SIZE):
	white_pawn = {'row': 0, 'column': 0}
	black_pawn = {'row': 0, 'column': 0}
	for row in range(FIELD_SIZE):
		current_row = input().split()
		board_array.append(current_row)
		if "w" in current_row:
			white_pawn['row'] = row
			white_pawn['column'] = current_row.index('w')
		if "b" in current_row:
			black_pawn['row'] = row
			black_pawn['column'] = current_row.index('b')
	return white_pawn, black_pawn


def check_taking(pawn_pos):
	take = False
	col = pawn_pos['column']
	positions = [(pawn_pos['row'], pawn_pos['column'] - 1), (pawn_pos['row'], pawn_pos['column'] + 1)]
	for el in positions:
		if 0 <= el[0] < FIELD_SIZE and 0 <= el[1] < FIELD_SIZE:
			if not board_array[el[0]][el[1]] == '-':
				take = True
				col = el[1]
				break
	return take, col


def move_pawn(pawn_pos, pawn_color: str):
	is_queen = False
	is_taken = False
	moving = {'white': -1, 'black': +1}
	pawn_type = {'white': 'w', 'black': 'b'}

	next_pos = {'row': pawn_pos['row'] + moving[pawn_color], 'column': pawn_pos['column']}
	is_taken, column = check_taking(next_pos)
	if is_taken:
		next_pos = {'row': next_pos['row'], 'column': column}
		return next_pos, is_taken, is_queen
	if 0 <= next_pos['row'] < FIELD_SIZE:
		board_array[next_pos['row']][next_pos['column']] = pawn_type[pawn_color]
		board_array[pawn_pos['row']][pawn_pos['column']] = '-'
	else:
		is_queen = True
		return pawn_pos, is_taken, is_queen

	return next_pos, is_taken, is_queen


FIELD_SIZE = 8
rows_name = {x: str(8 - x) for x in range(8)}
cols_name = {x: chr(97 + x) for x in range(8)}
board_array = []

white_pawn, black_pawn = read_matrix(FIELD_SIZE)
winner_pawn = ''
winner = ''
taken = False
queen = False
while True:
	white_pawn, taken, queen = move_pawn(white_pawn, 'white')
	if taken or queen:
		winner_pawn = white_pawn
		winner = 'White'
		break
	black_pawn, taken, queen = move_pawn(black_pawn, 'black')
	if taken or queen:
		winner_pawn = black_pawn
		winner = 'Black'
		break

winner_pawn_location = f"{cols_name[(winner_pawn['column'])]}{rows_name[(winner_pawn['row'])]}"
if queen:
	print(f"Game over! {winner} pawn is promoted to a queen at {winner_pawn_location}.")
else:
	print(f"Game over! {winner} win, capture on {winner_pawn_location}.")

# print(f"White pawn is on square {cols_name[(white_pawn['column'])]}{rows_name[(white_pawn['row'])]}")
# print(f"Black pawn is on square {cols_name[(black_pawn['column'])]}{rows_name[(black_pawn['row'])]}")
#


# prints
# print(rows_name)
# print(cols_name)
# print(f"Black pawn is on square{rows_name[]]}")
# pprint(board_array)
# print(white_pawn)
# print(black_pawn)
