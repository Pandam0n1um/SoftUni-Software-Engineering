starting_hour_exam = int(input())
starting_minute_exam = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

starting_minutes_converted = (starting_hour_exam * 60 + starting_minute_exam)

arrival_minute_converted = (arrival_hour * 60 + arrival_minute)

diff = abs(starting_minutes_converted - arrival_minute_converted)

if arrival_minute_converted < starting_minutes_converted and diff > 30:
    minutes_early = diff
    hours_early = diff // 60
    print("Early")
    if hours_early > 0:
        minutes_early = diff % 60
        print(f"{hours_early}:{minutes_early:02d} hours before the start ")
    else:
        print(f"{minutes_early} minutes before the start")


elif arrival_minute_converted <= starting_minutes_converted and diff <= 30:
    minutes_early = diff
    print(f"On time")
    if arrival_minute_converted == starting_minutes_converted:
        pass
    else:
        print(f"{minutes_early} minutes before the start")

    pass
elif arrival_minute_converted > starting_minutes_converted:
    minutes_late = diff
    hours_late = diff // 60
    print(f"Late")
    if hours_late > 0:
        minutes_late = diff % 60
        print(f"{hours_late}:{minutes_late:02d} hours after the start ")
    else:
        print(f"{minutes_late} minutes after the start")
