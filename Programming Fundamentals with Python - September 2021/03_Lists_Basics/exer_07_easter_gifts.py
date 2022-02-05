gifts_list = input().split()

command = input()

while not command == "No Money":
    command_list = command.split()
    current_gift = command_list[1]
    if command_list[0] == "OutOfStock":
        gifts_list[:] = ["None" if x == current_gift else x for x in gifts_list]
    elif command_list[0] == "Required":
        gift_index = int(command_list[2])
        if 0 <= gift_index < len(gifts_list):
            gifts_list[gift_index] = current_gift
    elif command_list[0] == "JustInCase":
        gifts_list[-1] = current_gift
    command = input()

try:
    while True:
        gifts_list.remove("None")
except ValueError:
    pass

gifts_list_string = ' '.join([str(elem) for elem in gifts_list])

print(gifts_list_string)

# 0<=