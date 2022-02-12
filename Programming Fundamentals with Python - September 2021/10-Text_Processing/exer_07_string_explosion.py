input = input()
result = ""
power = 0
for index, value in enumerate(input):
    if value == ">":
        power += int(input[index + 1])
        result += value
        continue
    if power > 0:
        power -= 1
    else:
        result += value

print(result)
