# player_pos = []
# matrix = []
# initial = list(input())
# size = int(input())
# for i in range(size):
# 	row = list(input())
# 	matrix.append(row)
# 	if "P" in row:
# 		player_pos = [i, row.index('P')]
# count = int(input())
#
#
# def moving(action, player_pos, string):
# 	directions = {
# 		'up': [-1, 0],
# 		'down': [1, 0],
# 		'left': [0, -1],
# 		'right': [0, 1],
# 	}
# 	new_pos = [x + y for x, y in zip(player_pos, directions[action])]
# 	if min(new_pos) < 0 or max(new_pos) >= size:
# 		string = string[:-1]
# 		return player_pos, player_pos, string
# 	elif not matrix[new_pos[0]][new_pos[1]] == '-':
# 		string += matrix[new_pos[0]][new_pos[1]]
# 	return player_pos, new_pos, string
#
#
# for i in range(count):
# 	action = input()
# 	old_cell, player_pos, initial = moving(action, player_pos, initial)
# 	if not old_cell == player_pos:
# 		matrix[old_cell[0]][old_cell[1]] = '-'
# 		matrix[player_pos[0]][player_pos[1]] = 'P'
# print(*initial, sep="")
# for row in matrix:
# 	print(*row, sep="")

def read_matrix(row):
	matrix = []
	for _ in range(row):
		matrix.append([el for el in input()])
	return matrix


def find_the_player(matrix, row):
	for i in range(row):
		for j in range(row):
			if matrix[i][j] == 'P':
				return i, j


def is_valid(row, inx, j):
	return 0 <= inx <= row - 1 and 0 <= j <= row - 1


def next_move(matrix, row, player_i, player_j):
	word = ''
	fail = False
	if is_valid(row, player_i, player_j):
		if not matrix[player_i][player_j] == '-':
			word += matrix[player_i][player_j]
	else:
		fail = True
	return player_i, player_j, fail, word


some_data = input()
size_field = int(input())

field = read_matrix(size_field)
player_row, player_col = find_the_player(field, size_field)
n = int(input())
initial_string = [el for el in some_data]

for _ in range(n):
	curr_r, curr_c = player_row, player_col
	command = input()
	letter = ''
	error = False
	field[player_row][player_col] = '-'
	if command == 'up':
		player_row, player_col, error, letter = next_move(field, size_field, player_row - 1, player_col)
	elif command == 'down':
		player_row, player_col, error, letter = next_move(field, size_field, player_row + 1, player_col)
	elif command == 'left':
		player_row, player_col, error, letter = next_move(field, size_field, player_row, player_col - 1)
	elif command == 'right':
		player_row, player_col, error, letter = next_move(field, size_field, player_row, player_col + 1)

	if error:
		if len(initial_string) > 0:
			initial_string.pop()
			player_row = curr_r
			player_col = curr_c
	elif isinstance(letter, str):
		initial_string.append(letter)
	field[player_row][player_col] = 'P'

print(''.join(initial_string))
for i in range(size_field):
	print(''.join(field[i]))
