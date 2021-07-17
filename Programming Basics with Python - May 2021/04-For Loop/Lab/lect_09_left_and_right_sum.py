n_times_2=int(input())
left_sum=0
right_sum=0
for num in range(n_times_2):
    left_input=int(input())
    left_sum+=left_input
for num in range(n_times_2):
    right_input=int(input())
    right_sum+=right_input
if left_sum==right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff=abs(left_sum-right_sum)
    print(f"No, diff = {diff}")

