input_list = input().split(", ")

result_list = [int(n) for n in input_list if not n == "0"]
result_list.extend([0] * input_list.count("0"))

print(result_list)
