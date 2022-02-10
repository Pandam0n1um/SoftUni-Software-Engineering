item = ""
dict_elem = {"shards": 0, "motes": 0, "fragments": 0}
weapon_dict = {"shards": "Shadowmourne", "motes": "Dragonwrath", "fragments": "Valanyr"}
junk = {}
is_found = False

while True:
    if is_found:
        break
    farming = input().lower().split()

    for i in range(0, len(farming), 2):
        elem = farming[i + 1]
        qty = int(farming[i])
        if elem in dict_elem:
            dict_elem[elem] += qty
            if dict_elem[elem] >= 250 and not is_found:
                dict_elem[elem] -= 250
                is_found = True
                item=weapon_dict[elem]
                break
        else:
            if elem not in junk:
                junk[elem] = qty
            else:
                junk[elem] += qty

dict_elem = dict(sorted(dict_elem.items(), key=lambda x: (-x[1], x[0])))
junk = dict(sorted(junk.items(), key=lambda x: x[0]))

if is_found:
    print(f"{item} obtained!")
for elem, qty in dict_elem.items():
    print(f"{elem}: {qty}")
for elem, qty in junk.items():
    print(f"{elem}: {qty}")
