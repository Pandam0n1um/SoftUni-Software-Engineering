def tribonacci_sequence(number):
    result=[1, 1, 2]
    if number>3:
        for index in range(number-3):
            summation=(result[-1]+result[-2]+result[-3])
            result.append(summation)
    else:
        result=result[:number]
    result_str=[str(elem) for elem in result]
    return result_str



num=int(input())


a=" ".join(tribonacci_sequence(num))

print(a)