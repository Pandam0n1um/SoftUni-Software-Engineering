integer_amount=int(input())

i=0
total_sum=0
while i<integer_amount:
    number_input=int(input())
    total_sum+=number_input
    i+=1
average_number= total_sum/integer_amount
print(f"{average_number:.2f}")