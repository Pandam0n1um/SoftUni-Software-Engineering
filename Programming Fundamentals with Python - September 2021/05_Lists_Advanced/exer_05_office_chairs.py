number_rooms=int(input())

total_free_chairs=0
are_enough=True

for rooms in range (1,number_rooms+1):
    room_details=input().split()
    current_free_chairs=len(room_details[0])-int(room_details[1])
    if current_free_chairs<0:
        are_enough=False
        print(f"{abs(current_free_chairs)} more chairs needed in room {rooms}")
    else:
        total_free_chairs+=current_free_chairs

if are_enough:
    print(f"Game On, {total_free_chairs} free chairs left")