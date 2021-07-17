amount_holidays = int(input())

amount_workdays = int(365 - amount_holidays)

minutes_playtime = int(amount_workdays * 63 + amount_holidays * 127)

if minutes_playtime <= 30000:
    minutes_playtime_needed_total=int(30000-minutes_playtime)
    hours_playtime_needed=(minutes_playtime_needed_total//60)
    minutes_playtime_needed=(minutes_playtime_needed_total%60)
    print("Tom sleeps well")
    print(f"{hours_playtime_needed} hours and {minutes_playtime_needed} minutes less for play")

else:
    minutes_playtime_played_total = int(minutes_playtime-30000)
    hours_playtime_played = (minutes_playtime_played_total // 60)
    minutes_playtime_played = (minutes_playtime_played_total % 60)
    print("Tom will run away")
    print(f"{hours_playtime_played} hours and {minutes_playtime_played} minutes more for play")

