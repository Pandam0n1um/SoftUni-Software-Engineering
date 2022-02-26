def read_board():
    # read chess board
    n = int(input())
    matrix = [list(input()) for _ in range(n)]
    return matrix


def knights_are_attacking_each_other(matrix):
    knight_positions = find_all_knights(matrix)

    for row, col in knight_positions:
        positions_to_check = [
            (row + 2, col - 1),
            (row + 2, col + 1),
            (row + 1, col - 2),
            (row + 1, col + 2),
            (row - 1, col - 2),
            (row - 1, col + 2),
            (row - 2, col - 1),
            (row - 2, col + 1),
        ]
        # we found a knight
        for position in positions_to_check:
            pos_row, pos_col = position
            if not 0 <= pos_row < len(matrix):
                continue
            if not 0 <= pos_col < len(matrix):
                continue
            if matrix[pos_row][pos_col] == "K":
                return True
    # we know the pos is inside
    return False


def find_all_knights(matrix):
    positions = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "K":
                positions.append((row, col))
    return positions


def calculate_aggression(matrix, knight_positions):
    aggresion_scores = {}
    for row, col in knight_positions:
        positions_to_check = [
            (row + 2, col - 1),
            (row + 2, col + 1),
            (row + 1, col - 2),
            (row + 1, col + 2),
            (row - 1, col - 2),
            (row - 1, col + 2),
            (row - 2, col - 1),
            (row - 2, col + 1),
        ]
        attacked_count = 0
        for attacked_row, attacked_col in positions_to_check:
            if not 0 <= attacked_row < len(matrix):
                continue
            if not 0 <= attacked_col < len(matrix):
                continue
            if matrix[attacked_row][attacked_col] == "K":
                attacked_count += 1
        aggresion_scores[(row, col)] = attacked_count
    return aggresion_scores


def find_max_aggression(aggression_scores):
    max_so_far = None
    for pos, aggression in aggression_scores.items():
        if not max_so_far or max_so_far < aggression:
            max_so_far = aggression
            max_pos = pos
    return max_pos


def main():
    matrix = read_board()
    deleted_knights_count = 0
    while knights_are_attacking_each_other(matrix) is True:
        #       find all knight positions
        knight_positions = find_all_knights(matrix)
        #       calculate aggression(how many other knigts are attacked by current)
        aggression_scores = calculate_aggression(matrix, knight_positions)
        #       delele the most aggresive one
        row, col = find_max_aggression(aggression_scores)

        # delete most aggressive knight
        matrix[row][col] = '0'
        deleted_knights_count += 1
    print(deleted_knights_count)


main()

# 9
# 0000K0000
# 000000000
# 00000K000
# 000000000
# K000K000K
# 00K000K00
# 000000000
# 000000000
# 000000000
