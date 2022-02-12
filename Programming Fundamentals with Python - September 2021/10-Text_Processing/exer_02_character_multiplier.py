str_1, str_2 = input().split()
result = 0
word = ""
if len(str_1) > len(str_2):
    word = str_1
else:
    word = str_2

length = max(len(str_1), len(str_2))
stop = min(len(str_1), len(str_2))
for i in range(stop):
    result += ord(str_1[i]) * ord(str_2[i])

for i in range(stop, length):
    result += (ord(word[i]))

print(result)
