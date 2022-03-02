def operate(action, *args):
    result = 0
    if action in ('*', '/'):
        result = 1

    for idx,val in enumerate(args):
        if action == "+":
            result += val
        elif action == "-":
            if idx==0:
                result = val
            else:
                result -= val
        elif action == "*":
            result *= val
        elif action == "/":
            if idx==0:
                result=val
            else:
                result /= val
    return result


print(operate("+", 1, 2, 3))
print(operate("/", 3, 4))
