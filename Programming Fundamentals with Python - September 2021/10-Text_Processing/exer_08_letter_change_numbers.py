input_line = input().split()
# input_line=" ".join(input_line)
# input_line=input_line.split()


result=[]
for elem in input_line:
    current = 0
    first_lowered = ord(elem[0].lower()) - 96
    second_lowered = ord(elem[-1].lower()) - 96
    number = int(elem[1:-1:])

    if elem[0].isupper():
        current += number / first_lowered
    else:
        current += number * first_lowered
    if elem[-1].isupper():
        current -= second_lowered
    else:
        current += second_lowered

    result.append(current)
print(f"{sum(result):.2f}")


#
# seq = input().split()
# total = 0
#
# for s in seq:
#     fletter = s[0]
#     sletter = s[-1]
#     fcode = ord(fletter.lower()) - 96
#     scode = ord(sletter.lower()) - 96
#
#     number = int(s[1:-1])
#     if fletter.islower():
#         current = number * fcode
#     else:
#         current = number / fcode
#
#     if sletter.islower():
#         current = current + scode
#     else:
#         current = current - scode
#
#     total += current
#
# print(f"{total:.2f}")


a = input().split()
b = ""
num = ""
total_sum = 0

for i in range(0, len(a)):
    b = str(a[i])
    num = str(b[1:len(b) - 1])
    a1 = b[0]
    b1 = b[len(b) - 1]
    if b[0].isupper():
        c = ord(a1) - 64
        mid_sum1 = int(num) / c
    else:
        c = ord(a1) - 96
        mid_sum1 = int(num) * c
    if b1.isupper():
        d = ord(b1) - 64
        mid_sum2 = mid_sum1 - d
    else:
        d = ord(b1) - 96
        mid_sum2 = d + mid_sum1
    total_sum += mid_sum2
print(f"{total_sum:.2f}")