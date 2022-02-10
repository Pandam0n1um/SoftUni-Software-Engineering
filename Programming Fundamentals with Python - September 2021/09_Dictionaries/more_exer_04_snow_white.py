# dwarf_dict = {}
#
# while True:
#     command = input()
#     if command == "Once upon a time":
#         break
#
#     dwarf_name, hat_color, dwarf_phys = command.split(" <:> ")
#     dwarf_phys = int(dwarf_phys)
#     if hat_color not in dwarf_dict:
#         dwarf_dict[hat_color] = {}
#
#     if dwarf_name in dwarf_dict[hat_color]:
#         curr_phys = dwarf_dict[hat_color][dwarf_name]
#         dwarf_dict[hat_color][dwarf_name] = max(curr_phys, dwarf_phys)
#     else:
#         dwarf_dict[hat_color][dwarf_name] = dwarf_phys
#
# # dwarf_sorted=
# print(dwarf_dict)


# dwarf_dict = {}
#
# while True:
#     command = input()
#     if command == "Once upon a time":
#         break
#
#     dwarf_name, hat_color, dwarf_phys = command.split(" <:> ")
#     dwarf_phys = int(dwarf_phys)
#     if dwarf_phys not in dwarf_dict:
#         dwarf_dict[dwarf_phys] = []
#
#     for height in dwarf_dict:
#         if dwarf_name in dwarf_dict[height][hat_color]:
#             if dwarf_phys > height:
#                 dwarf_dict[height].remove({hat_color: dwarf_name})
#                 dwarf_dict[dwarf_phys][hat_color].append(dwarf_name)
#         else:
#             dwarf_dict[dwarf_phys][hat_color].append(dwarf_name)
#
# dwarf_dict_sorted = dict(sorted(dwarf_dict.items(), key=lambda x: x[0], reverse=True))
# for height, dwarf in dwarf_dict_sorted.items():
#     if len(dwarf_dict_sorted[height]) > 0:
#         for i in range(len(dwarf_dict_sorted[height])):
#             color,name=dwarf_dict_sorted[height][i]
#             print(f'{color}) {name} <-> {height})')
# print(dwarf_dict_sorted)


class Dwarf:
    def __init__(self, name_s, color_s, physics_s, number_of_color, sequence):
        self.name = name_s
        self.color = color_s
        self.physics = physics_s
        self.number_of_color = number_of_color
        self.sequence = sequence

    def add_number_of_color(self, color_dict):
        if self.color in color_dict:
            self.number_of_color = color_dict[self.color]
            return self.number_of_color


counter_for_sequence = 1
list_of_objects = []
command = input()
color_dictionary = {}
while not command == "Once upon a time":
    name, color, physics = command.split(" <:> ")
    current_object = Dwarf(name, color, int(physics), 0, counter_for_sequence)
    if list_of_objects:
        for item in list_of_objects:
            if item.name == name and item.color == color and item.physics < int(physics):
                list_of_objects.remove(item)
                break
    list_of_objects.append(current_object)
    counter_for_sequence += 1
    command = input()
for item in list_of_objects:
    if item.color not in color_dictionary:
        color_dictionary[item.color] = 0
    color_dictionary[item.color] += 1
for item in list_of_objects:
    item.add_number_of_color(color_dictionary)
sorted_objects = sorted(list_of_objects, key=lambda x: (-x.physics, -x.number_of_color, x.sequence))
for item in sorted_objects:
    print(f"({item.color}) {item.name} <-> {item.physics}")

# content = input()
# drafts = {}
# color_name = {}
# while not content == "Once upon a time":
#     name, colour, physics = content.split(" <:> ")
#     draft = f"({colour}) {name}"
#     dwarf_physics = int(physics)
#     if draft not in drafts:
#         drafts[draft] = dwarf_physics
#     else:
#         if dwarf_physics > drafts[draft]:
#             drafts[draft] = dwarf_physics
#     if colour not in color_name:
#         color_name[colour] = [name]
#     else:
#         if name not in color_name[colour]:
#             color_name[colour].append(name)
#     content = input()
#
# sorted_colour_by_length = sorted(color_name.items(), key=lambda x: len(x[1]), reverse=True)
#
# new_draft = {}
# for color, names in sorted_colour_by_length:
#     for name in names:
#         dr = f"({color}) {name}"
#         new_draft[dr] = drafts[dr]
#
# drafts_sorted = sorted(new_draft.items(), key=lambda x: -x[1])
# for name, physics in drafts_sorted:
#     print(f"{name} <-> {physics}")