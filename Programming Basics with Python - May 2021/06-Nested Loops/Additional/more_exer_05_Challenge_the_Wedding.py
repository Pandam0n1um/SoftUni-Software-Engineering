amount_men=int(input())
amount_women=int(input())
amount_table=int(input())
counter_dates=0

for man in range (1, amount_men+1):
    for woman in range (1, amount_women+1):
        counter_dates+=1
        if counter_dates>amount_table:
            break
        else:
            print(f"({man} <-> {woman})",end=" ")