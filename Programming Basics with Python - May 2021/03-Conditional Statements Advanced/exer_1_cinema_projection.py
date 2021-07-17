type_projection = str(input().lower())

cinema_rows = int(input())

cinema_columns = int(input())

price_premiere_ticket = 12

price_normal_ticket = 7.50

price_discount = ticket = 5

seats_count = cinema_columns * cinema_rows

income = None

if type_projection == str('premiere'):
    income = price_premiere_ticket * seats_count
elif type_projection == str('normal'):
    income = price_normal_ticket * seats_count
elif type_projection == str('discount'):
    income = price_discount * seats_count
print(f'{income:.2f} leva')