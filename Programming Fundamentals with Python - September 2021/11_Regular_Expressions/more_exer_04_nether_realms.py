import re

participants = sorted(''.join(input().split()).split(','))
for p in participants:
    health = sum([ord(s) for s in re.findall(r'[^ 0-9-+*/.]', p)])
    numbers = re.findall(r'([-+]?\d+(\.\d+)?)', p)
    damage = sum([float(d[0]) for d in numbers])
    for i in range(p.count('/')): damage /= 2
    for i in range(p.count('*')): damage *= 2
    print(f"{p} - {health} health, {damage:.2f} damage")

# import re
#
# demon_book = {}
#
# demons = sorted(''.join(input().split()).split(','))
#
# for name in demons:
#     name_regex = r"[^\d+-/\*]"
#     numbers_regex = r"(?P<numbers>[+-]?[\d]+(.\d+)?)"
#     operator_regex = r"(?P<operations>[\*\/]+)"
#
#     health = sum([ord(x) for x in re.findall(name_regex, name)])
#     all_nums = re.finditer(numbers_regex, name)
#     damage=0
#     for num in all_nums:
#         value=num.group()
#         if "-" in value:
#             damage-=float(value[1:])
#             if damage<0:
#                 damage=0
#         elif "+" in value:
#             damage+=float(value[1:])
#         else:
#             damage+=float(value)
#
#     all_operators = "".join(re.findall(operator_regex, name))
#     for operation in all_operators:
#         if operation=="*":
#             damage*=2
#         else:
#             damage/=2
#     demon_book[name]={'health':health,'damage':damage}
#
# for demon,statistics in demon_book.items():
#     print(f"{demon} - {statistics['health']} health, {statistics['damage']:.2f} damage")
#
