from collections import deque


def read_matrix():
    matrix_size = int(input())
    matrix = [[int(j) for j in input().split()] for i in range(matrix_size)]
    return matrix


def explode_bombs(matrix, coordinates):
    while coordinates:
        bomb = coordinates.popleft()
        row, col = [int(el) for el in bomb.split(",")]
        bomb_value = matrix[row][col]
        if bomb_value<=0:
            continue
        for mod_row in range(-1, 2):
            for mod_col in range(-1, 2):
                curr_row = row + mod_row
                curr_col = col + mod_col
                # curr_pos=str(curr_row)+','+str(curr_col)
                if not (0 <= curr_row < len(matrix) and 0 <= curr_col < len(matrix)):
                    continue
                # if curr_pos in coordinates:
                #     continue
                cur_val = matrix[curr_row][curr_col]
                if cur_val <= 0:
                    continue
                matrix[curr_row][curr_col] -= bomb_value

    return matrix


def check_live_bombs(matrix):
    count_alive = 0
    sum_alive = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] > 0:
                count_alive += 1
                sum_alive += matrix[row][col]
    return count_alive, sum_alive


matrix = read_matrix()
coordinates = deque(input().split())

matrix = explode_bombs(matrix, coordinates)

count_alive, sum_alive = check_live_bombs(matrix)

print(f"Alive cells: {count_alive}")
print(f"Sum: {sum_alive}")

for row in (matrix):
    print(*row)