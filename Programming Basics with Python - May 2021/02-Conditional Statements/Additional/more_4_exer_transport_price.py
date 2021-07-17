travel_distance_km=int(input())

day_night=str(input())

taxi_init_price=0.7

taxi_day_tariff_km=0.79

taxi_night_tariff_km=0.9

bus_tariff_km=0.09

bus_distance_min_km=20

train_tariff_km=0.06

train_distance_min_km=100

taxi_cost_day=float(travel_distance_km*taxi_day_tariff_km+0.70)

taxi_cost_night=float(travel_distance_km*taxi_night_tariff_km+0.70)

bus_cost=float(travel_distance_km*bus_tariff_km)

train_cost=float(travel_distance_km*train_tariff_km)

if travel_distance_km<20 and day_night==("day"):
    print(f"{taxi_cost_day:.2f}")

elif travel_distance_km<20 and day_night==("night"):
    print(f"{taxi_cost_night:.2f}")

elif 20<=travel_distance_km<100:
    print(f"{bus_cost:.2f}")

elif 100<=travel_distance_km:
    print(f"{train_cost:.2f}")