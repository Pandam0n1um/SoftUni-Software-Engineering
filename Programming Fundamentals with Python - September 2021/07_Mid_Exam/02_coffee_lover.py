def include(new_coffee):
    coffee_list.append(new_coffee)
    return


def remove(position, length, coffees):
    length = int(length)
    if length > len(coffees):
        return coffees
    if position == "first":
        coffees = coffees[length::]
    else:
        coffees = coffees[:-length:]
    return coffees


def prefer(index1, index2, coffees):
    index1 = int(index1)
    index2 = int(index2)
    if index1 >= len(coffees) or index2 >= len(coffees):
        return coffees
    coffees[index1], coffees[index2] = coffees[index2], coffees[index1]
    return coffees


coffee_list = input().split()
number_commands = int(input())

for i in range(number_commands):
    command = input().split()
    action = command[0]
    if action == "Include":
        include(command[1])
    elif action == "Remove":
        coffee_list = remove(command[1], command[2], coffee_list)
    elif action == "Prefer":
        coffee_list = prefer(command[1], command[2], coffee_list)
    elif action == "Reverse":
        coffee_list=coffee_list[::-1]

print("Coffees:")
print(" ".join(coffee_list))
