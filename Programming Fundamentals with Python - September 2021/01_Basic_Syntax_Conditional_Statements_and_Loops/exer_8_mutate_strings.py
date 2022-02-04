str_1=input()

str_2=input()

n=len(str_1)

result=""

for index in range(0,n):
    for i in range (index+1):
        result+=str_2[i]
    for j in range(index+1,len(str_1)):
        result+=str_1[j]
    if not str_1[index]==str_2[index]:
        print(result)
    result=""