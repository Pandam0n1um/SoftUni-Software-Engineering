import re

sentence=input()
word=input()
pattern=fr"\b({word})\b"
occurencies=re.findall(pattern,sentence,re.IGNORECASE)

print(len(occurencies))