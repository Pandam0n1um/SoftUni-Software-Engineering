age = float(input())

gender = str(input().lower())

if gender == str('f'):
    if age < 16:
        print('Miss')
    else:
        print('Ms.')

elif gender == str('m'):
    if age < 16:
        print('Master')
    else:
        print('Mr.')
