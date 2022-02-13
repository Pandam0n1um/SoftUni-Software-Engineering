import re

pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-z]+-?[a-z]+(\.[a-z]+)+"

text=input()

valid_mails=[el.group() for el in re.finditer(pattern,text)]

print(*valid_mails, sep="\n")