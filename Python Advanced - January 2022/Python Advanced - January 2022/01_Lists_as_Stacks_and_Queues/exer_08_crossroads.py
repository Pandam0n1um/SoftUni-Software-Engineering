# from collections import deque
#
# green_duration = int(input())
# free_window = int(input())
#
# cars = deque()
# is_crash = False
# total_cars = 0
#
# while True:
#     command = input()
#     if command == "END":
#         break
#     if command == "green":
#         current_car = ""
#         crashed_car = ""
#         current_green = green_duration
#         current_window = free_window
#         while current_green > 0 and cars:
#             current_car = cars.popleft()
#             crashed_car = current_car
#             remaining_seconds = current_green - len(current_car)
#             if remaining_seconds > 0:
#                 current_green -= len(current_car)
#                 total_cars += 1
#             else:
#                 if remaining_seconds == 0:
#                     total_cars += 1
#                     current_car = None
#                     break
#                 current_car = current_car[remaining_seconds:]
#                 break
#         if current_car:
#             diff = current_window - len(current_car)
#             if diff < 0:
#                 is_crash = True
#                 print("A crash happened!")
#                 print(f"{crashed_car} was hit at {current_car[diff]}.")
#                 break
#             else:
#                 total_cars += 1
#                 break
#
#     else:
#         cars.append(command)
#
# if not is_crash:
#     print("Everyone is safe.")
#     print(f"{total_cars} total cars passed the crossroads.")

# from collections import deque
#
# green_light = int(input())
# window = int(input())
#
# cars = deque()
# cars_counter = 0
# crashed = False
#
# command = input()
#
# while command != "END":
#     if command == "green":
#         if cars:
#             current = cars.popleft()
#             seconds_left = green_light - len(current)
#             while seconds_left > 0:
#                 cars_counter += 1
#                 if cars:
#                     current = cars.popleft()
#                     seconds_left -= len(current)
#                 else:
#                     break
#             if seconds_left == 0:
#                 cars_counter += 1
#             if window >= abs(seconds_left):
#                 if seconds_left < 0:
#                     cars_counter += 1
#             else:
#                 idx = window + seconds_left
#                 print("A crash happened!")
#                 print(f"{current} was hit at {current[idx]}.")
#                 crashed = True
#                 break
#     else:
#         cars.append(command)
#     command = input()
#
# if not crashed:
#     print("Everyone is safe.")
#     print(f"{cars_counter} total cars passed the crossroads.")


from collections import deque

green_duration = int(input())
free_window = int(input())

cars = deque()
is_crash = False
total_cars = 0

while True:
    command = input()
    if command == "END":
        break
    if command == "green":
        current_car = ""
        crashed_car = ""
        current_green = green_duration
        current_window = free_window
        while current_green > 0 and cars:
            current_car = cars.popleft()
            crashed_car = current_car
            remaining_seconds = current_green - len(current_car)
            if remaining_seconds > 0:
                current_green -= len(current_car)
                total_cars += 1
                current_car = None
            else:
                if remaining_seconds == 0:
                    total_cars += 1
                    current_car = None
                    current_green = 0
                    break
                current_car = current_car[remaining_seconds:]
                current_green = 0
        while current_window >= 0 and current_car:
            diff = current_window - len(current_car)
            if diff < 0:
                is_crash = True
                print("A crash happened!")
                print(f"{crashed_car} was hit at {current_car[diff]}.")
                break
            else:
                total_cars += 1
                current_car=None
        if is_crash:
            break

    else:
        cars.append(command)

if not is_crash:
    print("Everyone is safe.")
    print(f"{total_cars} total cars passed the crossroads.")
