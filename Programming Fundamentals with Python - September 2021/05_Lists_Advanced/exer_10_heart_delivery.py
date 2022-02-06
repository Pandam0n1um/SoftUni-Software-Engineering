house_list = [int(i) for i in input().split("@")]
position = 0
while True:
    command = input()
    if command == "Love!":
        break
    command_list = command.split()
    jump_value = int(command_list[1])
    position += jump_value
    if position > len(house_list)-1:
        position = 0
    if house_list[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        house_list[position] -= 2
        if house_list[position] == 0:
            print(f"Place {position} has Valentine's day.")

valentine_house_list = [house for house in house_list if not house == 0]

print(f"Cupid's last position was {position}.")

if len(valentine_house_list)>0:
    print(f"Cupid has failed {len(valentine_house_list)} places.")
else:
    print("Mission was successful.")
