time_first = int(input())

time_second = int(input())

time_third = int(input())

total_time = (time_first + time_second + time_third)

result_minutes = (total_time // 60)

result_seconds = (total_time % 60)

if result_seconds < 10:
    print(f"{result_minutes}:0{result_seconds}")
else:
    print(f"{result_minutes}:{result_seconds}")
