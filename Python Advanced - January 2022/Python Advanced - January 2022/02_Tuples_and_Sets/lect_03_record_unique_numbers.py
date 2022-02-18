count = int(input())

names = set()

for _ in range(count):
    name = input()
    names.add(name)

[print(el) for el in names]
