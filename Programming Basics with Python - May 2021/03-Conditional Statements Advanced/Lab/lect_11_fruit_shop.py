fruit_type = str(input().lower())
weekday = str(input().lower())
amount = float(input())

weekday_check=None
price = None

if weekday == str('monday') or weekday == str('monday') or weekday == str('tuesday') or weekday == str(
        'wednesday') or weekday == str('thursday') or weekday == str('friday'):
    if fruit_type == str('banana'):
        price = 2.50
    elif fruit_type == str('apple'):
        price = 1.20
    elif fruit_type == str('orange'):
        price = 0.85
    elif fruit_type == str('grapefruit'):
        price = 1.45
    elif fruit_type == str('kiwi'):
        price = 2.70
    elif fruit_type == str('pineapple'):
        price = 5.50
    elif fruit_type == str('grapes'):
        price = 3.85
    else:
        price = 0

elif weekday == str('saturday') or weekday == str('sunday'):
    if fruit_type == str('banana'):
        price = 2.70
    elif fruit_type == str('apple'):
        price = 1.25
    elif fruit_type == str('orange'):
        price = 0.90
    elif fruit_type == str('grapefruit'):
        price = 1.60
    elif fruit_type == str('kiwi'):
        price = 3.00
    elif fruit_type == str('pineapple'):
        price = 5.60
    elif fruit_type == str('grapes'):
        price = 4.20
    else:
        price = 0
else:
    weekday_check=0

if weekday_check==0 or price==0:
    print('error')
else:
    total_cost=price*amount
    print(f'{total_cost:.2f}')