def shoot(tar_list, tar_index, tar_power):
    if 0 <= tar_index < len(tar_list):
        tar_list[tar_index] -= tar_power
        if tar_list[tar_index] <= 0:
            tar_list.pop(tar_index)
    return tar_list


def add_operation(tar_list, tar_index, tar_value):
    if 0 <= tar_index < len(tar_list):
        tar_list.insert(tar_index, tar_value)
    else:
        print("Invalid placement!")
    return tar_list


def strike_operation(tar_list, tar_index, tar_radius):
    end = tar_index + tar_radius
    start = tar_index - tar_radius
    if start >= 0 and end < len(tar_list):
        for n in range(end, start - 1, -1):
            tar_list.pop(n)
    else:
        print("Strike missed!")
    return tar_list


target_list = [int(i) for i in input().split()]

while True:
    input_command = input().split()
    operation = input_command[0]

    if operation == "End":
        break
    target_index = int(input_command[1])
    target_value = int(input_command[2])

    if operation == "Shoot":
        target_list = shoot(target_list, target_index, target_value)

    elif operation == "Add":
        target_list = add_operation(target_list, target_index, target_value)

    elif operation == "Strike":
        target_list = strike_operation(target_list, target_index, target_value)

target_list = [str(i) for i in target_list]

print("|".join(target_list))
