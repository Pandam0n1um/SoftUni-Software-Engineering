def exchange(input_list, index_pos):
    index_pos = int(index_pos)
    exchanged_list = input_list[index_pos + 1:]
    list_appendix = input_list[:index_pos + 1]
    exchanged_list.extend(list_appendix)
    return exchanged_list


def work_list(even_odd, working_list=[]):
    if even_odd == "even":
        working_list = [num for num in init_list if num % 2 == 0]
    elif even_odd == "odd":
        working_list = [num for num in init_list if not num % 2 == 0]
    return working_list


def index_finder(input_list, list_value):
    final_index = max(index for index, item in enumerate(input_list) if item == list_value)
    return final_index


def ult_value(max_min, even_odd, ultimate_value=None):
    current_list = work_list(even_odd)
    if max_min == "max":
        ultimate_value = max(current_list, default="Not_found")
    else:
        ultimate_value = min(current_list, default="Not_found")
    if not ultimate_value == "Not_found":
        print(index_finder(init_list, ultimate_value))
    else:
        print("No matches")
    return


def first_last(domain, index, even_odd, n_count_list=[]):
    n_count_list = work_list(even_odd)
    if domain == "first":
        print(n_count_list[:index:])
    else:
        print(n_count_list[-index::])


init_list = [int(num) for num in input().split()]

while True:
    command = input().split()
    action = command[0]
    if action == "end":
        break
    elif action == "exchange":
        index_value = int(command[1])
        if not (index_value >= len(init_list) or index_value < 0):
            init_list = exchange(init_list, command[1])
        else:
            print("Invalid index")
    elif action == "max" or action == "min":
        ult_value(action, command[1])
    elif action == "first" or action == "last":
        count_value = int(command[1])
        if not (count_value > len(init_list)):
            first_last(action, count_value, command[2])
        else:
            print("Invalid count")

print(init_list)
