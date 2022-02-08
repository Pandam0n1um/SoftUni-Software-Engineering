import math


def closest_to_center(x1: float, x2: float, y1: float, y2: float):
    x_distance_from_center = math.sqrt((x1 ** 2) + (x2 ** 2))
    y_distance_from_center = math.sqrt((y1 ** 2) + (y2 ** 2))
    if y_distance_from_center < x_distance_from_center:
        return f'({math.floor(y1)}, {math.floor(y2)})'
    else:
        return f'({math.floor(x1)}, {math.floor(x2)})'


def farthest_from_center(x1: float, x2: float, y1: float, y2: float):
    x_distance_from_center = math.sqrt((x1 ** 2) + (x2 ** 2))
    y_distance_from_center = math.sqrt((y1 ** 2) + (y2 ** 2))
    if y_distance_from_center > x_distance_from_center:
        return f'({math.floor(y1)}, {math.floor(y2)})'
    else:
        return f'({math.floor(x1)}, {math.floor(x2)})'


def line_length(n1_x: float, n1_y: float, n2_x: float, n2_y: float):
    distance = math.sqrt((n2_x - n1_x) ** 2 + (n2_y - n1_y) ** 2)
    return distance


def take_line_coordinates():
    p1_x = float(input())
    p1_y = float(input())
    p2_x = float(input())
    p2_y = float(input())
    return [p1_x, p1_y, p2_x, p2_y]


line_one = take_line_coordinates()
line_two = take_line_coordinates()

line_one_length = line_length(line_one[0], line_one[1], line_one[2], line_one[3])
line_two_length = line_length(line_two[0], line_two[1], line_two[2], line_two[3])

if line_one_length >= line_two_length:
    print(closest_to_center(line_one[0], line_one[1], line_one[2], line_one[3]), end='')
    print(farthest_from_center(line_one[0], line_one[1], line_one[2], line_one[3]))
else:
    print(closest_to_center(line_two[0], line_two[1], line_two[2], line_two[3]), end='')
    print(farthest_from_center(line_two[0], line_two[1], line_two[2], line_two[3]))
