last_sector_letter=input()
count_rows_first=int(input())
count_odd_seats=int(input())

counter_total_seats=0

for sector in range(ord("A"), ord(last_sector_letter)+1):
    for rows in range(1,count_rows_first+1):
        if rows%2==0:
            seats_per_row=count_odd_seats+2
        else:
            seats_per_row=count_odd_seats
        for seats in range(97,97+seats_per_row):
            print(f"{chr(sector)}{rows}{chr(seats)}")
            counter_total_seats+=1
    count_rows_first+=1

print(counter_total_seats)