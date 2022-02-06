numbers_list = input().split(".")
number=int("".join(numbers_list))
number+=1
result=[a for a in str(number)]

print(".".join(result))