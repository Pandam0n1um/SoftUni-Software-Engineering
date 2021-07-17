weather_degrees = float(input())

if 26 <= weather_degrees <= 35:
    print(f'Hot')
elif 20.1 <= weather_degrees <= 25.9:
    print(f'Warm')

elif 15.0 <= weather_degrees <= 20.00:
    print(f'Mild')
elif 12.0 <= weather_degrees <= 14.9:
    print(f'Cool')
elif 5.0 <= weather_degrees <= 11.9:
    print(f'Cold')
else:
    print(f"unknown")
