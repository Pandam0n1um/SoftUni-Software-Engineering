dragon_count = int(input())
dr_dict = {}
dr_armor = ""
for dragon in range(dragon_count):
    dr_type, dr_name, dr_damage, dr_health, dr_armor = input().split()
    values = [dr_damage, dr_health, dr_armor]
    keys_list = ["dr_damage", "dr_health", "dr_armor"]
    curr = {k: int(v) for (k, v) in (zip(keys_list, values)) if not v == "null"}
    curr.setdefault("dr_damage", 45)
    curr.setdefault("dr_health", 250)
    curr.setdefault("dr_armor", 10)
    if dr_type not in dr_dict:
        dr_dict[dr_type] = {}
    dr_dict[dr_type][dr_name] = curr.copy()

for dragon_type, dragon_name in dr_dict.items():
    count=len(dragon_name)
    avg_damage = sum([dragon["dr_damage"] for dragon in dragon_name.values()])/count
    avg_health = sum([dragon["dr_health"] for dragon in dragon_name.values()])/count
    avg_armor = sum([dragon["dr_armor"] for dragon in dragon_name.values()])/count

    print(f"{dragon_type}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")

    dr_name_sorted = sorted(dragon_name.items(), key=lambda x: x[0])
    for dr in dr_name_sorted:
        print(f"-{dr[0]} -> damage: {dr[1]['dr_damage']}, health: {dr[1]['dr_health']}, armor: {dr[1]['dr_armor']}")