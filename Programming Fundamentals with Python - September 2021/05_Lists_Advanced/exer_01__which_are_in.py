substrings = input().split(", ")
unique_list = input().split(", ")

occ_substrings = []

# resulting_list=list(filter(lambda x,num: substrings[x] in x, unique_list))

for substr in substrings:
    for word in unique_list:
        if substr in occ_substrings:
            continue
        if not substr in word:
            continue
        occ_substrings.append(substr)

# print(sorted(set(occ_substrings), key=occ_substrings.index))

print(occ_substrings)

