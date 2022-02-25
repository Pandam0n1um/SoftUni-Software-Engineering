import re
text=input()
# while True:
#     if not "  " in text:
#         break
#     text=text.replace("  "," ")


matrix=[[x for x in el.split()] for el in text.split("|")]

a=[" ".join(el) for el in matrix[::-1] if el]
print(*a)
# a=matrix[::-1]
# print(*a)
# print(*(matrix[::-1]))