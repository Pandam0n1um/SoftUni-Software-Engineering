import re

pattern=r"(\+359 2 \d{3} \d{4}\b)|(\+359-2-\d{3}-\d{4}\b)"

text=input()

matches=re.finditer(pattern,text)

valid_numbers=list([match.group() for match in matches])

print(", ".join(valid_numbers))
