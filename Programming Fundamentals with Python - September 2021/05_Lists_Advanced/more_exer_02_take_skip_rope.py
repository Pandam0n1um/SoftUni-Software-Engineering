input_list = list(input())

num_val_list = [num_val for num_val in input_list if str(num_val).isnumeric()]
non_num_val_list = [num_val for num_val in input_list if not str(num_val).isnumeric()]

take_list = num_val_list[::2]
skip_list = num_val_list[1::2]
taken_list = []
while True:
    if len(take_list) == 0:
        break

    length_taken = take_list.pop(0)
    length_skipped = skip_list.pop(0)
    taken_string = non_num_val_list[:int(length_taken)]
    taken_list.extend(taken_string)
    del non_num_val_list[:int(length_taken)]
    skipped_string = non_num_val_list[:int(length_skipped):]
    del non_num_val_list[:int(length_skipped)]


result="".join(taken_list)
print(result)
