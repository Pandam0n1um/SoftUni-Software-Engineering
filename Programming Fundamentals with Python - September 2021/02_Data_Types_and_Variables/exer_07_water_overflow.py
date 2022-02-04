lines_count = int(input())

tank_volume = 255

for i in range(lines_count):
    water_quantity = int(input())
    if tank_volume >= water_quantity:
        tank_volume -= water_quantity
    else:
        print(f"Insufficient capacity!")

water_left=255-tank_volume
print(water_left)