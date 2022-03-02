def permutations(values, index):
    if index == len(values):
        print(''.join(values))
        return
    for i in range(index, len(values)):
        values[i], values[index] = values[index], values[i]
        permutations(values, index + 1)
        values[i], values[index] = values[index], values[i]


chars = list(input())
permutations(chars, 0)
