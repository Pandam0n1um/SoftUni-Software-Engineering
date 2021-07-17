import math

current_world_record = float(input())

distance_meters = float(input())

time_for_1_m = float(input())

drag_time = float(math.floor(distance_meters / 15)* 12.5)

total_time = float(time_for_1_m * distance_meters + drag_time)

if total_time < current_world_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    seconds_left = (total_time - current_world_record)
    print(f"No, he failed! He was {seconds_left:.2f} seconds slower.")
