days=int(input())
daily_plunder=int(input())
expected_plunder=float(input())
total=0

for day in range(1,days+1):
    if day%3==0:
        total+=daily_plunder*1.5
    else:
        total+=daily_plunder
    if day%5==0:
        total*=0.7
percentage=total/expected_plunder*100
if total<expected_plunder:
    print(f"Collected only {percentage:.2f}% of the plunder.")
else:
    print(f"Ahoy! {total:.2f} plunder gained.")