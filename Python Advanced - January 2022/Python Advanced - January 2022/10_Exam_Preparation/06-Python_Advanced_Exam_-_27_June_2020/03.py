def numbers_searching(*args):
    result=[]
    args = sorted(args)
    left_limit = args[0]
    right_limit =args[-1]
    no_dupl = set(args)
    dupl=[]
    missing=None
    for el in range(left_limit,right_limit+1):
        if el not in args:
            missing=el
    result.append(missing)
    for el in no_dupl:
        if args.count(el)>1:
            dupl.append(el)
    dupl=sorted(dupl)
    result.append(dupl)
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
