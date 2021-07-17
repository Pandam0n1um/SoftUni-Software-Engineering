green_paint_consumption = 3.4

red_paint_consumption = 4.3

x_x_wall_door = float(1.2 * 2)

x_y_wall_window = float(1.5 * 1.5)

x_house = float(input())

y_house = float(input())

h_house = float(input())

x_x_wall = float(x_house * x_house)

x_y_wall = float(x_house * y_house)

x_h_wall = float(x_house * h_house / 2)

green_walls_area = float(2 * x_y_wall + 2 * x_x_wall - x_x_wall_door - 2 * x_y_wall_window)

red_walls_area = float(2 * x_y_wall + 2 * x_h_wall)

green_paint_quant = float(green_walls_area / green_paint_consumption)

red_paint_quant = float(red_walls_area / red_paint_consumption)

print(f"{green_paint_quant:.2f}")

print(f"{red_paint_quant:.2f}")