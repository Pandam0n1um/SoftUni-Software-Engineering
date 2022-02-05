import math


def orientation_calc(list_oriented):
    distance_point_1 = math.sqrt(list_oriented[0][0] ** 2 + list_oriented[0][1] ** 2)
    distance_point_2 = math.sqrt(list_oriented[1][0] ** 2 + list_oriented[1][1] ** 2)
    if distance_point_1 > distance_point_2:
        list_oriented = list_oriented[::-1]
    return list_oriented


def line_length_calc(point_1, point_2):
    length = math.sqrt((point_1[0] - point_2[0]) ** 2 + ((point_1[1] - point_2[1]) ** 2))

    return length


def longest_line_calc(point):
    longest_distance = 0
    longest_line_list =[]
    for n in range(lines_count):
        point_1 = point[2 * n]
        point_2 = point[2 * n + 1]
        line_length = line_length_calc(point_1, point_2)
        if line_length > longest_distance or line_length==0:
            longest_distance = line_length
            longest_line_list = [point_1, point_2]
    return longest_line_list


list_points = []
lines_count = 2

for lines in range(lines_count):
    for points in range(2):
        val_x = float(input())
        val_y = float(input())
        points_coord = [val_x, val_y]
        list_points.append(points_coord)

longest_line = longest_line_calc(list_points)

longest_line = orientation_calc(longest_line)

print(f"({math.floor(longest_line[0][0])}, {math.floor(longest_line[0][1])})({math.floor(longest_line[1][0])}, {math.floor(longest_line[1][1])})")

# print(f"({' '.join([str(elem) for elem in longest_line[0]]})")

# print(line_length_calc(longest_line[0],longest_line[1]))
