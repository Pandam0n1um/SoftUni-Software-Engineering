first_pos = int(input())
second_pos = int(input())
third_pos = int(input())
if second_pos>7:
    second_pos=7

for first in range(1,first_pos+1):
    for second in range(2,second_pos+1):
        is_prime = True
        counter_prime = 0
        for i in range(1,second+1):
            if second % i == 0:
                counter_prime += 1
            if counter_prime > 2:
                is_prime = False
                continue
        for third in range(1,third_pos+1):
            if (first % 2 == 0) and is_prime and (third%2==0):
                print(f"{first} {second} {third}")