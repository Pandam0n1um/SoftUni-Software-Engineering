input = input()
result = []
current = ""
for i in range(len(input)):
    a=input[i]
    b=""
    if input[i].isnumeric():
        a=input[i]
        if input[i-1].isnumeric():
            continue
        elif i<len(input)-1:
            if input[i+1].isnumeric():
                b=input[i+1]
        repeated=int(a+b)
        result.append(current * int(repeated))
        current = ""
    else:
        current += a
result = "".join(result).upper()
set_input = set(result)

print(f"Unique symbols used: {len(set_input)}")
print(result)


# input = input()
# result = []
# current = ""
# for char in input:
#     if char.isnumeric():
#         result.append(current * int(char))
#         current = ""
#     else:
#         current += char
# result = "".join(result).upper()
# set_input = set(result)
#
# print(f"Unique symbols used: {len(set_input)}")
# print(result)