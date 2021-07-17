count_1_lev=int(input())
count_2_lev=int(input())
count_5_lev=int(input())
total_money=int(input())


for coin_1_lev in range(count_1_lev+1):
    for coin_2_lev in range(count_2_lev+1):
        for note_5_Lev in range (count_5_lev+1):
            sum_to_check=(coin_1_lev*1+coin_2_lev*2+note_5_Lev*5)
            if sum_to_check==total_money:
                print(f"{coin_1_lev} * 1 lv. + {coin_2_lev} * 2 lv. + {note_5_Lev} * 5 lv. = {total_money} lv.")
