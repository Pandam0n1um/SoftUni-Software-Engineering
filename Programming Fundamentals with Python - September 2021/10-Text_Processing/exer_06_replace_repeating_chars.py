string = input()

new_string =[string[0]]
# print(string)
i = 0
for letter in string:
    if not letter==new_string[-1]:
        new_string.append(letter)
print("".join(new_string))
