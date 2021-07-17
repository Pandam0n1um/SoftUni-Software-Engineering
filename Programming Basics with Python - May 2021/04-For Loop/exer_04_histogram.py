numbers_amount = int(input())

p1_counter=0
p2_counter=0
p3_counter=0
p4_counter=0
p5_counter=0

for number in range(numbers_amount):
    number_input=int(input())
    if number_input<200:
        p1_counter+=1
    elif 200<=number_input<400:
        p2_counter+=1
    elif 400<=number_input<600:
        p3_counter+=1
    elif 600<=number_input<800:
        p4_counter+=1
    elif 800<=number_input:
        p5_counter+=1

ratio_p1=(p1_counter/numbers_amount)*100
ratio_p2=(p2_counter/numbers_amount)*100
ratio_p3=(p3_counter/numbers_amount)*100
ratio_p4=(p4_counter/numbers_amount)*100
ratio_p5=(p5_counter/numbers_amount)*100

print(f"{ratio_p1:.2f}%")
print(f"{ratio_p2:.2f}%")
print(f"{ratio_p3:.2f}%")
print(f"{ratio_p4:.2f}%")
print(f"{ratio_p5:.2f}%")