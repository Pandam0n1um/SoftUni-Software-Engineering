import re

pattern = r"\d+"
text_line = input()
all=""
while not text_line == "":
    all += text_line
    text_line=input()

matches = re.findall(pattern, all)

print(*matches)