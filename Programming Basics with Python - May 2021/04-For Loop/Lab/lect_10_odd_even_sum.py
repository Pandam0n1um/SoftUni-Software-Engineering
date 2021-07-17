n_times_2=int(input())
odd_sum=0
even_sum=0
for num in range(n_times_2):
    number_input=int(input())
    if num%2==0:
        even_sum+=number_input
    else:
        odd_sum+=number_input

if odd_sum == even_sum:
    print(f"""Yes
Sum = {odd_sum}""")
else:
    diff = abs(odd_sum - even_sum)
    print(f"""No
Diff = {diff}""")
