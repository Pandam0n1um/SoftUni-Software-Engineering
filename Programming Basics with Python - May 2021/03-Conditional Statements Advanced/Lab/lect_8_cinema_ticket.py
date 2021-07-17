weekday = str(input().lower())

if weekday == str('monday') or weekday == str('tuesday') or weekday == str('friday'):
    print('12')

elif weekday == str('wednesday') or weekday == str('thursday'):
    print('14')

elif weekday == str('saturday') or weekday == str('sunday'):
    print('16')