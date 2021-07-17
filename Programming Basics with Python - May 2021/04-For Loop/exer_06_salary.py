amount_open_tabs=int(input())
salary=int(input())
is_salary_lost=False

for n in range(amount_open_tabs):
    tab_name=str(input())
    if tab_name=="Facebook":
        salary-=150
    elif tab_name=="Instagram":
        salary-=100
    elif tab_name=="Reddit":
        salary-=50

    if salary<=0:
        is_salary_lost=True
        break

if is_salary_lost:
    print("You have lost your salary.")
else:
    print(f"{salary}")
