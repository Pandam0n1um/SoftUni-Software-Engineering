trip_duration_days = int(input())

room_type = str(input())

review_type = str(input())

trip_duration_nights = (trip_duration_days-1)

price_room_for_one = 18

price_apartment = 25

price_president_apartment = 35

price_night=None

if room_type==str('room for one person'):
    price_night = price_room_for_one

elif room_type==str('apartment'):
    if trip_duration_days<10:
        price_night = (price_apartment * 0.7)
    elif 10<=trip_duration_days<=15:
        price_night=(price_apartment*0.65)
    elif 15<trip_duration_days:
        price_night=(price_apartment*0.5)

elif room_type == str('president apartment'):
    if trip_duration_days < 10:
        price_night = (price_president_apartment * 0.9)
    elif 10 <= trip_duration_days <= 15:
        price_night = (price_president_apartment * 0.85)
    elif 15 < trip_duration_days:
        price_night = (price_president_apartment * 0.8)

cost_trip_nominal=price_night*trip_duration_nights
cost_trip_total=None

if review_type==str('positive'):
    cost_trip_total=(cost_trip_nominal*1.25)
elif review_type==str('negative'):
    cost_trip_total = (cost_trip_nominal * 0.9)

print(f'{cost_trip_total:.2f}')