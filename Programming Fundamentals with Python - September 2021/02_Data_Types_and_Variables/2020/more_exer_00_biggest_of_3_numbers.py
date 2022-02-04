import sys
max_value=-sys.maxsize
for i in range (3):
    value_input=int(input())
    if value_input>max_value:
        max_value=value_input

print(max_value)