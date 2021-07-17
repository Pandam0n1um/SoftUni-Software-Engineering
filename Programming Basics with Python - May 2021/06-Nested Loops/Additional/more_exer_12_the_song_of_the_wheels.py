control_value_M=int(input())
password_counter=0
fourth_password=None
is_fourth_found=False
for first in range (1,10):
    for second in range(1, 10):
        for third in range(1, 10):
            for fourth in range(1, 10):
                check_sum=(first*second+third*fourth)
                is_relation = False
                if first<second and third>fourth:
                    is_relation=True
                if check_sum==control_value_M and is_relation:
                    password_counter+=1
                    print(f"{first}{second}{third}{fourth} ")
                    if password_counter==4:
                        fourth_password=f"{first}{second}{third}{fourth}"
                        is_fourth_found=True
if is_fourth_found:
    print(f"Password: {fourth_password}")
else:
    print("No!")