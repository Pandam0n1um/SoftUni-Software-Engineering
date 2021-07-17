weekday = str(input().lower())

if weekday == str('monday') or weekday == str('tuesday') or weekday == str('wednesday') or weekday == str('thursday')\
        or weekday == str('friday'):
    print('Working day')
elif weekday==('saturday') or weekday==('sunday'):
    print('Weekend')

else:
    print('Error')
