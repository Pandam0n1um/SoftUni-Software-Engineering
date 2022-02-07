items_list = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break
    command=command.split()
    action=command[0]
    item = command[1]

    if action == "Urgent":
        if not item in items_list:
            items_list.insert(0, item)
    elif action == "Unnecessary":
        if item in items_list:
            items_list.remove(item)
    elif action == "Correct":
        new_item = command[2]
        if item in items_list:
            index = items_list.index(item)
            items_list[index] = new_item
    elif action == "Rearrange":
        if item in items_list:
            index = items_list.index(item)
            rearranged = items_list.pop(index)
            items_list.append(rearranged)

print(", ".join(items_list))