import re

pattern = r"(^_|(?<=\s_))[a-zA-Z0-9]+\b"

text=input()

valid_variables=[obj.group() for obj in re.finditer(pattern,text)]

print(*valid_variables, sep=",")