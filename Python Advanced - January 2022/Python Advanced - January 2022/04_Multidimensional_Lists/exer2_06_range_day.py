def is_inside(temp_pos):
    if (0 <= min(temp_pos)) and (max(temp_pos) < len(shooting_range)):
        return True
    return False


def moving(direction, steps, pos):
    move = {'up': (-steps, 0), 'down': (steps, 0), 'right': (0, steps), 'left': (0, -steps)}
    temp_pos = tuple(map(sum, zip(pos, move[direction])))
    if is_inside(temp_pos) and shooting_range[temp_pos[0]][temp_pos[1]] == ".":
        shooting_range[temp_pos[0]][temp_pos[1]] = 'A'
        shooting_range[pos[0]][pos[1]] = "."
        pos = temp_pos

    return pos


def shooting(direction, pos, targets):
    move = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}
    while True:
        temp_pos = tuple(map(sum, zip(pos, move[direction])))
        boundaries = is_inside(temp_pos)
        if boundaries and shooting_range[temp_pos[0]][temp_pos[1]] == "x":
            shooting_range[temp_pos[0]][temp_pos[1]] = '.'
            targets_shot.append(temp_pos)
            targets -= 1
            break
        if not boundaries:
            break
        pos = temp_pos

    return targets


LINES = 5
shooting_range = []
curr_pos = ()
target_count = 0
targets_shot = []
for row in range(LINES):
    curr_row = input().split()
    shooting_range.append(curr_row)
    if 'A' in curr_row:
        curr_pos = (row, curr_row.index('A'))
    if "x" in curr_row:
        target_count += curr_row.count('x')
initial_target_count = target_count
comm_count = int(input())

for command in range(comm_count):
    action, *tokens = input().split()
    if action == "move":
        curr_pos = moving(tokens[0], int(tokens[1]), curr_pos)
    elif action == "shoot":
        target_count = shooting(tokens[0], curr_pos, target_count)
    if target_count == 0:
        break

if target_count > 0:
    print(f"Training not completed! {target_count} targets left.")
else:
    print(f"Training completed! All {initial_target_count} targets hit.")
for coord in targets_shot:
    print(f"[{coord[0]}, {coord[1]}]")

# from pprint import pprint
#
#
# def is_inside(temp_pos):
# 	if (0 <= min(temp_pos)) and (max(temp_pos) < len(shooting_range)):
# 		return True
# 	return False
#
#
# def moving(direction, steps, pos):
# 	move = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}
# 	for step in range(steps):
# 		temp_pos = tuple(map(sum, zip(pos, move[direction])))
# 		if is_inside(temp_pos) and shooting_range[temp_pos[0]][temp_pos[1]] == ".":
# 			shooting_range[temp_pos[0]][temp_pos[1]] = 'A'
# 			shooting_range[pos[0]][pos[1]] = "."
# 			pos = temp_pos
# 		else:
# 			break
# 	return pos
#
#
# def shooting(direction, pos, targets):
# 	move = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}
# 	while True:
# 		temp_pos = tuple(map(sum, zip(pos, move[direction])))
# 		boundaries = is_inside(temp_pos)
# 		if boundaries and shooting_range[temp_pos[0]][temp_pos[1]] == "x":
# 			shooting_range[temp_pos[0]][temp_pos[1]] = '.'
# 			targets_shot.append(temp_pos)
# 			targets -= 1
# 			break
# 		if not boundaries:
# 			break
# 		pos = temp_pos
#
# 	return targets
#
#
# LINES = 5
# shooting_range = []
# curr_pos = ()
# target_count = 0
# targets_shot = []
# for row in range(LINES):
# 	curr_row = input().split()
# 	shooting_range.append(curr_row)
# 	if 'A' in curr_row:
# 		curr_pos = (row, curr_row.index('A'))
# 	if "x" in curr_row:
# 		target_count += curr_row.count('x')
# initial_target_count = target_count
# comm_count = int(input())
#
# for command in range(comm_count):
# 	action, *tokens = input().split()
# 	if action == "move":
# 		curr_pos = moving(tokens[0], int(tokens[1]), curr_pos)
# 	elif action == "shoot":
# 		target_count = shooting(tokens[0], curr_pos, target_count)
# 	if target_count==0:
# 		break
#
# if target_count > 0:
# 	print(f"Training not completed! {target_count} targets left.")
# else:
# 	print(f"Training completed! All {initial_target_count} targets hit.")
# for coord in targets_shot:
# 	print(f"[{coord[0]}, {coord[1]}]")
