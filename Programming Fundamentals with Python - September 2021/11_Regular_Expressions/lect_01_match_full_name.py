import re

names=input()

pattern=r"\b[A-Z][a-z]+\b \b[A-Z][a-z]+\b"

x=re.findall(pattern,names)

print(*x)

