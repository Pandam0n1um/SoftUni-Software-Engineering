daynight_hour = int(input())

weekday = str(input().lower())

if 10 <= daynight_hour <= 18:
    if weekday == str('monday') or weekday == str('tuesday') or weekday == str('wednesday') or weekday == str(
            'thursday') or weekday == str('friday') or weekday == str('saturday'):
        print("open")
    else:
        print("closed")
else:
    print("closed")

