product = str(input().lower())

city = str(input().lower())

quantity = float(input())

price = None

if city == str('sofia'):
    if product == str('coffee'):
        price = 0.50
    elif product == str('water'):
        price = 0.80
    elif product == str('beer'):
        price = 1.20
    elif product == str('sweets'):
        price = 1.45
    elif product == str('peanuts'):
        price = 1.60
elif city == str('plovdiv'):
    if product == str('coffee'):
        price = 0.40
    elif product == str('water'):
        price = 0.70
    elif product == str('beer'):
        price = 1.15
    elif product == str('sweets'):
        price = 1.30
    elif product == str('peanuts'):
        price = 1.50
elif city == str('varna'):
    if product == str('coffee'):
        price = 0.45
    elif product == str('water'):
        price = 0.70
    elif product == str('beer'):
        price = 1.10
    elif product == str('sweets'):
        price = 1.35
    elif product == str('peanuts'):
        price = 1.55

cost=(price*quantity)

print(cost)

