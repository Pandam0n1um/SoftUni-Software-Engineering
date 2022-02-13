import re

pattern = r"w{3}\.[a-zA-Z0-9-]+(\.[\.a-z]+)"
valids=[]
while True:
    text=input()
    if not text:
        break
    valid_domains=[domain.group() for domain in re.finditer(pattern,text)]
    if valid_domains:
        valids.extend(valid_domains)
print(*valids,sep="\n")