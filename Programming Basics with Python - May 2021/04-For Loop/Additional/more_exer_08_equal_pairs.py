pairs_count=int(input())
sum_check=0
diff_max=0
is_equal=True
for pairs in range (pairs_count):
    number_1=int(input())
    number_2=int(input())
    sum_current= number_1 + number_2
    if pairs<1:
        sum_check=sum_current
    if not sum_check == sum_current:
        is_equal=False
        diff_current=abs(sum_check - sum_current)
        if diff_current>diff_max:
            diff_max=diff_current
        sum_check=sum_current

if is_equal:
    print(f"Yes, value={sum_current}")
else:
    print(f"No, maxdiff={diff_max}")
