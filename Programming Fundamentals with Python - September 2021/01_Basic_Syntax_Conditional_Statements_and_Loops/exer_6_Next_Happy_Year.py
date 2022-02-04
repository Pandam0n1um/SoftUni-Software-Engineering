input_year = int(input())

# is_distinct = False
#
# input_year += 1
#
# while not is_distinct:
#     year_string = str(input_year)
#     if len(year_string) == len(set(year_string)):
#         is_distinct = True
#         print(year_string)
#     input_year += 1

is_distinct = False
input_year += 1
while not is_distinct:
    thousands = input_year // 1000
    hundreds = (input_year // 100) % 10
    tenths = (input_year // 10) % 10
    units = input_year % 10

    if not (
            thousands == hundreds or thousands == tenths or thousands == units or hundreds == tenths or hundreds == units or tenths == units):
        is_distinct = True
        print(input_year)
    else:
        input_year += 1

# print(thousands)
# print(hundreds)
# print(tenths)
# print(units)
