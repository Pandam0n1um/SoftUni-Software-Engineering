temp_degrees = int(input())

time_of_day = str(input().lower())

outfit = None
shoes = None

if time_of_day == str('morning'):
    if 10 <= temp_degrees <= 18:
        outfit = str('Sweatshirt')
        shoes = str('Sneakers')
    elif 18 < temp_degrees <= 24:
        outfit = str('Shirt')
        shoes = str('Moccasins')
    elif temp_degrees >= 25:
        outfit = str('T-Shirt')
        shoes = str('Sandals')

elif time_of_day == str('afternoon'):
    if 10 <= temp_degrees <= 18:
        outfit = str('Shirt')
        shoes = str('Moccasins')
    elif 18 < temp_degrees <= 24:
        outfit = str('T-Shirt')
        shoes = str('Sandals')
    elif temp_degrees >= 25:
        outfit = str('Swim Suit')
        shoes = str('Barefoot')


elif time_of_day == str('evening'):
    outfit = str('Shirt')
    shoes = str('Moccasins')

print(f"It's {temp_degrees} degrees, get your {outfit} and {shoes}.")