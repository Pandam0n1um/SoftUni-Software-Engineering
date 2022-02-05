import math


def closest_point(x_val, y_val):
    distance = math.sqrt(x_val ** 2 + y_val ** 2)
    return distance


val_x_1 = float(input())
val_y_1 = float(input())
val_x_2 = float(input())
val_y_2 = float(input())

distance_1 = closest_point(val_x_1, val_y_1)
distance_2 = closest_point(val_x_2, val_y_2)

if distance_1 <= distance_2:
    print(f"({math.floor(val_x_1)}, {math.floor(val_y_1)})")
else:
    print(f"({math.floor(val_x_2)}, {math.floor(val_y_2)})")

# print(distance_1)
# print(distance_2)
