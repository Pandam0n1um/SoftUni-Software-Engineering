import sys

input_info = str(input())

min_number = sys.maxsize

while not input_info == str("Stop"):
    input_number = int(input_info)
    if input_number<min_number:
        min_number = input_number
    input_info = str(input())

print(f"{min_number}")
