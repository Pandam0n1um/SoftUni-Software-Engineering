import math

shape = str(input())

if shape == str('square'):
    a_square = float(input())
    area_square = float(a_square * a_square)
    print(f"{area_square:.3f}")

elif shape == str('rectangle'):
    a_rect = float(input())
    b_rect = float(input())
    area_rect = float(a_rect * b_rect)
    print(f"{area_rect:.3f}")

elif shape == str('circle'):
    radius_circle = float(input())
    area_circle = float(math.pi * radius_circle * radius_circle)
    print(f"{area_circle:.3f}")

elif shape == str('triangle'):
    a_triangle = float(input())
    h_triangle = float(input())
    area_triangle = float(a_triangle * h_triangle / 2)
    print(f"{area_triangle:.3f}")

