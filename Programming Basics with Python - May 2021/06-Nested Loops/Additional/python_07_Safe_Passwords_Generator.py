# value_a=int(input())
# value_b=int(input())
# max_amount_passwords=int(input())
# counter_passwords=0
# for first in range(35,55):
#     for second in range(64,97):
#         for third in range(1,value_a+2):
#             if third>value_a+1:
#                 exit()
#             for fourth in range(1,value_b+2):
#                 if fourth>value_b+1:
#                     exit()
#                 counter_passwords+=1
#                 if counter_passwords>max_amount_passwords:
#                     break
#                 print(f"{chr(first)}{chr(second)}{third}{fourth}{chr(second)}{chr(first)}", end="|")
#         if second>97:
#             second=64
#     if first>55:
#         first=35


value_a = int(input())
value_b = int(input())
max_amount_passwords = int(input())
counter_passwords = 0
first = 34
second = 63

for third in range(1, value_a + 1):
    if third > value_a:
        exit()
    for fourth in range(1, value_b + 1):
        first += 1
        second += 1
        if fourth > value_b:
            exit()
        counter_passwords += 1
        if counter_passwords > max_amount_passwords:
            exit()
        print(f"{chr(first)}{chr(second)}{third}{fourth}{chr(second)}{chr(first)}", end="|")

        if second == 96:
            second = 34
        if first == 55:
            first = 63
