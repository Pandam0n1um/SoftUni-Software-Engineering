vertex_1_x = float(input())
vertex_1_y = float(input())
vertex_2_x = float(input())
vertex_2_y = float(input())
point_x = float(input())
point_y = float(input())

border_check = None

if vertex_1_x == point_x or vertex_2_x == point_x:
    if vertex_1_y <= point_y <= vertex_2_y:
        border_check = 1
    else:
        border_check = 0
elif vertex_1_y == point_y or vertex_2_y == point_y:
    if vertex_1_x <= point_x <= vertex_2_x:
        border_check = 1
    else:
        border_check = 0

if border_check == 1:
    print(f"Border")
else:
    print(f"Inside / Outside")
