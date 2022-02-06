def collect(inventory_list, item_value):
    if item_value not in inventory_list:
        inventory_list.append(item_value)
    return inventory_list


def drop(inventory_list, item_value):
    if item_value in inventory_list:
        inventory_list.remove(item_value)
    return inventory_list


def combine(inventory_list, item_value):
    new_old_item = item_value.split(":")
    old_item = new_old_item[0]
    new_item = new_old_item[1]

    if old_item in inventory_list:
        input_index = inventory_list.index(old_item) + 1
        inventory_list.insert(input_index, new_item)

    return inventory_list


def renew(inventory_list, item_value):
    if item_value in inventory_list:
        inventory_list.append(inventory_list.pop(inventory_list.index(item_value)))
    return inventory_list


inventory = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break
    command = command.split(" - ")
    action = command[0]
    item = command[1]
    if action == "Collect":
        inventory = list(collect(inventory, item))
    elif action == "Drop":
        inventory = list(drop(inventory, item))
    elif action == "Combine Items":
        inventory = list(combine(inventory, item))
    elif action == "Renew":
        inventory = list(renew(inventory, item))

print(", ".join(inventory))
