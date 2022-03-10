def matrix_read():
    bucket = {}
    array = []
    for row in range(6):
        line = input().split()
        array.append(line)
        for col, val in enumerate(line):
            if val == "B":
                bucket[(row, col)] = True
    return bucket, array


def hit_bucket(current):
    if current in buckets and buckets.get(current):
        buckets[current] = False
        curr_col = current[1]
        # print(curr_col)
        total = sum([int(matrix[row][current[1]]) for row in range(6) if matrix[row][current[1]].isnumeric()])
        # print(total)
    else:
        total = 0
    return total


def present_check(score):
    if score < 100:
        return f"Sorry! You need {100 - score} points more to win a prize."
    else:
        prize = 'Lego Construction Set'
        for el, data in GIFTS_DICT.items():
            if data['range'][0] <= score:
                prize = el

        return f"Good job! You scored {score} points, and you've won {prize}."


GIFTS_DICT = {
    'Football': {'range': [100, 199]},
    'Teddy Bear': {'range': [200, 299]},
    'Lego Construction Set': {'range': [300]}
}

buckets, matrix = matrix_read()

points = 0

for i in range(3):
    row, column = [int(x) for x in input()[1:-1].split(', ')]
    throw = (row, column)
    points += hit_bucket(throw)

print(present_check(points))
