season = str(input())
group_type = str(input())
group_size = int(input())
night_count = int(input())

night_cost = None
sport_activity_type = None

if group_type == str("boys"):
    if season == str("Winter"):
        sport_activity_type = str("Judo")
        night_cost = 9.60
    elif season == str("Spring"):
        sport_activity_type = str("Tennis")
        night_cost = 7.20
    elif season == str("Summer"):
        sport_activity_type = str("Football")
        night_cost = 15.00

elif group_type == str("girls"):
    if season == str("Winter"):
        sport_activity_type = str("Gymnastics")
        night_cost = 9.60
    elif season == str("Spring"):
        sport_activity_type = str("Athletics")
        night_cost = 7.20
    elif season == str("Summer"):
        sport_activity_type = str("Volleyball")
        night_cost = 15.00

elif group_type == str("mixed"):
    if season == str("Winter"):
        sport_activity_type = str("Ski")
        night_cost = 10.00
    elif season == str("Spring"):
        sport_activity_type = str("Cycling")
        night_cost = 9.50
    elif season == str("Summer"):
        sport_activity_type = str("Swimming")
        night_cost = 20.00

total_cost_nominal = (group_size * night_cost*night_count)
total_cost = None
if 50 <= group_size:
    total_cost = (total_cost_nominal * 0.50)
elif 20 <= group_size < 50:
    total_cost = (total_cost_nominal * 0.85)
elif 10 <= group_size < 20:
    total_cost = (total_cost_nominal * 0.95)
else:
    total_cost=total_cost_nominal

print(f"{sport_activity_type} {total_cost:.2f} lv.")
