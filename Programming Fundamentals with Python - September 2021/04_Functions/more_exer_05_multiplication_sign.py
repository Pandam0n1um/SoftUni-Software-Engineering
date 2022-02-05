def sign(num1,num2,num3):
    negative_counter=0
    is_zero=False
    if num1<0:
        negative_counter+=1
    elif num1==0:
        is_zero=True
    if num2<0:
        negative_counter += 1
    elif num2==0:
        is_zero=True
    if num3<0:
        negative_counter += 1
    elif num3==0:
        is_zero=True
    if is_zero:
        return "zero"
    elif negative_counter%2==0:
        return"positive"
    else:
        return "negative"

num_1=float(input())
num_2=float(input())
num_3=float(input())

result=sign(num_1,num_2,num_3)

print(result)