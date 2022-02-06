from statistics import mean

empl_happiness = [int(el) for el in input().split()]

# employees_happiness_mapped = list(map(int,input().split()))

factor = int(input())

multiplied_happiness = [num * factor for num in empl_happiness]

avg_happiness = mean(multiplied_happiness)

# happy_employees=[h for h in multiplied_happiness if h >= avg_happiness]

# happy_employees=[]
# for h in multiplied_happiness:
#     if h>=avg_happiness:
#         happy_employees.append(h)
#
happy_employees = list(filter(lambda h: h >= avg_happiness, multiplied_happiness))

half_n = len(multiplied_happiness) / 2

if len(happy_employees) >= half_n:
    print(f"Score: {len(happy_employees)}/{len(multiplied_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(multiplied_happiness)}. Employees are not happy!")
