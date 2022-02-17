equation=input()
parenthesis=[]
for i,v in enumerate(equation):
    if v=="(":
        parenthesis.append(i)
    elif v==")" and parenthesis:
        end=i
        start=parenthesis.pop()
        print(equation[start:end+1])
