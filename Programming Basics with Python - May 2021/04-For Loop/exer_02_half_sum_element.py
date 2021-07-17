import sys
integer_count=int(input())
max_number=-sys.maxsize-1
min_number=sys.maxsize
sum=0

for num in range(integer_count):
    new_number=int(input())
    if new_number>max_number:
        max_number=new_number
    if new_number<min_number:
        min_number=new_number
    sum+=new_number

check_sum=sum-max_number

is_halfsum=(check_sum==max_number)
diff=abs(check_sum-max_number)

if is_halfsum:
    print(f"""Yes
Sum = {max_number}""")
else:
    print(f"""No
Diff = {diff}""")