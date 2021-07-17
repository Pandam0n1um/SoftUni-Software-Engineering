import math
L_hall = float(input())
W_hall = float(input())
A_wardrobe = float(input())

area_hall_cm = float(L_hall * W_hall * 100 * 100)

area_wardrobe = (A_wardrobe * A_wardrobe * 100 * 100)

area_bench = float(area_hall_cm * 0.1)

area_hall_free = float(area_hall_cm - area_wardrobe - area_bench)

number_of_dancers = float(area_hall_free / 7040)

print(math.floor(number_of_dancers))

#########

L_hall = float(input())
W_hall = float(input())
A_wardrobe = float(input())

area_hall_cm = float(L_hall * W_hall * 100 * 100)

area_wardrobe = (A_wardrobe * A_wardrobe * 100 * 100)

area_bench = float(area_hall_cm * 0.1)

area_hall_free = float(area_hall_cm - area_wardrobe - area_bench)

number_of_dancers = float(area_hall_free / 7040)

print(f"{number_of_dancers:.0f}")

L_hall = float(input())
W_hall = float(input())
A_wardrobe = float(input())

area_hall_cm = float(L_hall * W_hall * 100 * 100)

area_wardrobe = (A_wardrobe * A_wardrobe * 100 * 100)

area_bench = float(area_hall_cm * 0.1)

area_hall_free = float(area_hall_cm - area_wardrobe - area_bench)

number_of_dancers = int(area_hall_free // (7040))

print(number_of_dancers)


