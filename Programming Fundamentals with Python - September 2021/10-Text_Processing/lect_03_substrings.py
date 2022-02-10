substr=input()
line_str=input()
while substr in line_str:
    line_str=line_str.replace(substr,"")

print(line_str)