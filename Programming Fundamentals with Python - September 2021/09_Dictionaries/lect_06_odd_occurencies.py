words = input().lower().split()

dict = {}

for word in words:
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1

list_elem = [x for x in dict.keys() if dict[x] % 2 == 1]
print(*list_elem)

# print(words)
# print(dict)
