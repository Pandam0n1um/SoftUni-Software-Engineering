def index_check(command_list, counter, elem_list, is_index_valid=True, ):
    list_len = len(elem_list)
    if command_list[0] == command_list[1]:
        is_index_valid = False
    if command_list[0] < 0 or command_list[0] >= list_len or command_list[1] < 0 or command_list[1] >= list_len:
        is_index_valid = False
    if not is_index_valid:
        first_half = elem_list[:len(elem_list) // 2:]
        middle_list = 2 * ["-"+str(counter) + "a"]
        second_half = elem_list[len(elem_list) // 2::]
        elem_list = first_half + middle_list + second_half
        print("Invalid input! Adding additional elements to the board")
    return is_index_valid,elem_list


element_list = input().split()
is_complete = 0
moves_counter = 0
while True:
    command = input().split()
    moves_counter += 1
    if command[0] == "end":
        break
    command = [int(i) for i in command]
    command = sorted(command)
    first_pos = command[0]
    second_pos = command[1]

    is_index,element_list = index_check(command, moves_counter,element_list)

    if element_list[first_pos] == element_list[second_pos]:
        element_list.pop(second_pos)
        found_el = element_list.pop(first_pos)
        print(f"Congrats! You have found matching elements - {found_el}!")
    elif is_index:
        print("Try again!")
    if len(element_list) == 0:
        print(f"You have won in {moves_counter} turns!")
        exit()


print("Sorry you lose :(")
print(" ".join(element_list))
