snowbalL_count=int(input())

print_snowball_value=0
print_snowball_snow=0
print_snowball_time=0
print_snowball_quality=0
for i in range (1, snowbalL_count+1):
    snowball_snow=int(input())
    snowball_time=int(input())
    snowball_quality=int(input())

    snowball_value=pow((snowball_snow/snowball_time),snowball_quality)
    if snowball_value>print_snowball_value:
        print_snowball_snow=snowball_snow
        print_snowball_time=snowball_time
        print_snowball_quality=snowball_quality
        print_snowball_value=snowball_value

print(f"{print_snowball_snow} : {print_snowball_time} = {print_snowball_value:.0f} ({print_snowball_quality})")
