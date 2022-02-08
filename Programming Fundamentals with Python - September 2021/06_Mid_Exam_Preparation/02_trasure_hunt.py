def Loot(work_list):
    for i in range(len(work_list)):
        if work_list[i] not in loot_list:
            loot_list.insert(0, work_list[i])


def Drop(value):
    dropped = loot_list.pop(value)
    loot_list.append(dropped)


def Steal(value, input_list):
    reduced_list = input_list[:-value:]
    stolen_list = input_list[-value::]
    print(", ".join(stolen_list))
    return reduced_list


def Concat(work_list):
    average_value = 0
    list_length = len("".join(work_list))
    if list_length > 0:
        average_value = list_length / len(work_list)

    return list_length, average_value


loot_list = input().split("|")

while True:
    command = input().split()
    action = command[0]
    if action == "Yohoho!":
        break
    working_list = command[1::]
    working_index = working_list[0]

    if action == "Loot":
        Loot(working_list)
    elif action == "Drop":
        working_index = int(working_index)
        if 0 <= working_index < len(loot_list):
            Drop(working_index)
    elif action == "Steal":
        working_index = int(working_index)
        loot_list = Steal(working_index, loot_list)
length, average_value = Concat(loot_list)

if length <= 0:
    print("Failed treasure hunt.")

else:
    print(f"Average treasure gain: {average_value:.2f} pirate credits.")
