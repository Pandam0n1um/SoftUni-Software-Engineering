from pprint import pprint


def read_matrix(size):
	player = {'row': 0, 'column': 0}
	for row in range(size):
		current_row = input().split()
		coin_array.append(current_row)
		if "P" in current_row:
			player['row'] = row
			player['column'] = current_row.index('P')
	return player


def moving(direction: str, player_pos):
	is_valid = True
	new_coins = 0
	instructions = {
		'left': [0, -1],
		'right': [0, 1],
		'up': [-1, 0],
		'down': [1, 0]
	}

	new_player_row = adjust_coordinates(player_pos['row'] + instructions[direction][0])
	new_player_col = adjust_coordinates(player_pos['column'] + instructions[direction][1])

	new_player_pos = {
		'row': new_player_row,
		'column': new_player_col
	}
	if coin_array[new_player_row][new_player_col] == 'X':
		is_valid = False
	elif coin_array[new_player_row][new_player_col].isdigit():
		new_coins = int(coin_array[new_player_row][new_player_col])
		coin_array[new_player_row][new_player_col]='0'

	return is_valid, new_player_pos, new_coins


def adjust_coordinates(value):
	if value < 0:
		value += MATRIX_SIZE
	elif value >= MATRIX_SIZE:
		value -= MATRIX_SIZE
	return value


coin_array = []
coins_collected = 0
player_path=[]
directions_validity = ['up', 'down', 'left', 'right']

MATRIX_SIZE = int(input())
player_pos = read_matrix(MATRIX_SIZE)
player_path.append((player_pos['row'],player_pos['column']))

while True:
	if coins_collected >= 100:
		break
	command = input()
	if command not in directions_validity:
		continue
	valid_oper, player_pos, new_coins = moving(command, player_pos)
	player_path.append((player_pos['row'], player_pos['column']))
	if valid_oper:
		coins_collected+=new_coins
	else:
		coins_collected//=2
		break
if coins_collected>=100:
	print(f"You won! You've collected {coins_collected} coins.")
else:
	print(f"Game over! You've collected {coins_collected} coins.")

printed_path="Your path:"
for cell in player_path:
	printed_path+=f"\n[{cell[0]}, {cell[1]}]"

print(printed_path)


# pprint(coin_array)
# print(player_pos)
# print(coins_collected)
# print(player_path)

# def moving(direction, player_pos):
#     instructions = {
#         'left': [0, -1],
#         'right': [0, 1],
#         'up': [-1, 0],
#         'down': [1, 0]
#     }
#     new_pos = [x + y for x, y in zip(instructions[direction], player_pos)]
#     if min(new_pos) < 0:
#         for idx, val in enumerate(new_pos):
#             if val < 0:
#                 new_pos[idx] = FIELD_SIZE - 1
#     elif max(new_pos) >= FIELD_SIZE:
#         for idx, val in enumerate(new_pos):
#             if new_pos[idx] >= FIELD_SIZE:
#                 new_pos[idx] = 0
#     elif matrix[new_pos[0]][new_pos[1]] == 'X':
#         return 'End', new_pos
#     return int(matrix[new_pos[0]][new_pos[1]]), new_pos
#
#
# def reading_input(FIELD_SIZE):
#     player = []
#     array = []
#     for row in range(FIELD_SIZE):
#         curr_row = input().split()
#         array.append(curr_row)
#         if 'P' in curr_row:
#             player = [row, curr_row.index('P')]
#     return array, player
#
#
# FIELD_SIZE = int(input())
#
# matrix, player_pos = reading_input(FIELD_SIZE)
# player_path = []
# total_score = 0
# is_enough = False
# while True:
#     direction = input()
#     score, player_pos = moving(direction, player_pos)
#     if score == 'End':
#         total_score = total_score // 2
#         break
#     else:
#         total_score += score
#         player_path.append(player_pos)
#     if total_score >= 100:
#         is_enough = True
#         break
#
# if is_enough:
#     print(f"You won! You've collected {total_score} coins.")
# else:
#     print(f"Game over! You've collected {total_score} coins.")
# print(f"Your path:", *player_path, sep='\n')
#

# print(player_path)

# ___________________________________________
# Old task

# def moving(direction, player_pos):
#     instructions = {
#         'left': [0, -1],
#         'right': [0, 1],
#         'up': [-1, 0],
#         'down': [1, 0]
#     }
#     new_pos = [x + y for x, y in zip(instructions[direction], player_pos)]
#     if min(new_pos) < 0 or max(new_pos) >= FIELD_SIZE:
#         return 'End', new_pos
#     elif matrix[new_pos[0]][new_pos[1]] == 'X':
#         return 'End', new_pos
#     else:
#         return int(matrix[new_pos[0]][new_pos[1]]), new_pos
#
#
# def reading_input(FIELD_SIZE):
#     player = []
#     array = []
#     for row in range(FIELD_SIZE):
#         curr_row = input().split()
#         array.append(curr_row)
#         if 'P' in curr_row:
#             player = [row, curr_row.index('P')]
#     return array, player
#
#
# FIELD_SIZE = int(input())
#
# matrix, player_pos = reading_input(FIELD_SIZE)
# player_path = []
# total_score = 0
# is_enough = False
# while True:
#     direction = input()
#     score, player_pos = moving(direction, player_pos)
#     if score == 'End':
#         total_score = total_score // 2
#         break
#     else:
#         total_score += score
#         player_path.append(player_pos)
#     if total_score >= 100:
#         is_enough = True
#         break
#
# if is_enough:
#     print(f"You won! You've collected {total_score} coins.")
# else:
#     print(f"Game over! You've collected {total_score} coins.")
# print(f"Your path:", *player_path, sep='\n')
# # print(player_path)
