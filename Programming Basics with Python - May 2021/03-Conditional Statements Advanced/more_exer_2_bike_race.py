count_junior_participants = int(input())
count_senior_participants = int(input())
track_type = str(input())

total_participants = (count_senior_participants + count_junior_participants)

cost_junior = None
cost_senior = None

if track_type == str("trail"):
    cost_junior = 5.50
    cost_senior = 7

elif track_type == str("cross-country"):
    cost_junior = 8
    cost_senior = 9.50
    if 50 <= total_participants:
        cost_junior = (cost_junior * 0.75)
        cost_senior = (cost_senior * 0.75)

elif track_type == str("downhill"):
    cost_junior = 12.25
    cost_senior = 13.75

elif track_type == str("road"):
    cost_junior = 20
    cost_senior = 21.50

total_income=(cost_junior*count_junior_participants+cost_senior*count_senior_participants)*0.95

print(f"{total_income:.2f}")
