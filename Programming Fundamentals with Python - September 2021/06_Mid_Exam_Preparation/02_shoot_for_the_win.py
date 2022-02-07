value_list = [int(i) for i in input().split()]
shot_counter = 0
shot_index_list = []
while True:
    command = input()
    if command == "End":
        break
    tar_index = int(command)
    if tar_index not in shot_index_list and 0 <= tar_index < len(value_list):
        tar_value = value_list.pop(tar_index)
        value_list.insert(tar_index, -1)
        for count, curr_value in enumerate(value_list):
            if count == tar_index:
                continue
            if curr_value == -1:
                continue
            elif curr_value <= tar_value:
                value_list[count] += tar_value
            else:
                value_list[count] -= tar_value
        shot_counter += 1
        value_list[tar_index] = -1

value_list = [str(i) for i in value_list]
print(f"Shot targets: {shot_counter} ->", end=" ")
print(" ".join(value_list))
