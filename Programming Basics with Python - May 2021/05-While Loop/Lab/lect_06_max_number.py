import sys

input_info = str(input())

max_number = -sys.maxsize

while not input_info == str("Stop"):
    input_number = int(input_info)
    if input_number>max_number:
        max_number = input_number
    input_info = str(input())

print(f"{max_number}")
