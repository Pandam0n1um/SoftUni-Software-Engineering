import math

leap_normal = str(input())

holidays_p = int(input())

weekends_h = int(input())

total_days_played = None

total_weekends=48

sofia_weekends=(total_weekends-weekends_h)

sofia_weekends_volleyball=(sofia_weekends*3/4)

total_weekends_volleyball=(sofia_weekends_volleyball+weekends_h)

total_days_played=(total_weekends_volleyball+(holidays_p*2/3))

if leap_normal == str("normal"):
    total_days_played=total_days_played
elif leap_normal == str("leap"):
    total_days_played=(total_days_played*1.15)

print(f"{math.floor(total_days_played)}")