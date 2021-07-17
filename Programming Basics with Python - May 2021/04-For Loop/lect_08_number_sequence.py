import sys
count_numbers = int(input())
sum_numbers = 0
max_number=-sys.maxsize
min_number=sys.maxsize

for num in range(count_numbers):
    new_number = int(input())
    sum_numbers += new_number
    if new_number>max_number:
        max_number=new_number
    if new_number<min_number:
        min_number=new_number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")