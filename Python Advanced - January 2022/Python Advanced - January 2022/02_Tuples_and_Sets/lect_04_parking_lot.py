count = int(input())

car_numbers = set()

for _ in range(count):
    command, number = input().split(", ")
    if command=="IN":
        car_numbers.add(number)
    else:
        car_numbers.discard(number)

if car_numbers:
    [print(el) for el in car_numbers]
else:
    print("Parking Lot is Empty")