inheritance_sum=float(input())
year_of_death=int(input())
counter_years=18


for years in range (1800,year_of_death+1):
    if years%2==0:
        inheritance_sum-=12000
    else:
        inheritance_sum-=(12000+50*counter_years)
    counter_years += 1

if inheritance_sum>=0:
    print(f"Yes! He will live a carefree life and will have {inheritance_sum:.2f} dollars left.")
else:
    print(f"He will need {abs(inheritance_sum):.2f} dollars to survive.")