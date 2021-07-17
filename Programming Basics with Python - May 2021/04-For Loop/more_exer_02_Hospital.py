time_range = int(input())
doctors = 7
untreated_patients = 0
treated_patients = 0
for days in range(1, time_range + 1):
    if treated_patients < untreated_patients and (days % 3) == 0:
        doctors+=1

    current_day_patients = int(input())
    if current_day_patients>doctors:
        untreated_patients += current_day_patients - doctors
    if current_day_patients>doctors:
        treated_patients += doctors
    else:
        treated_patients+=current_day_patients
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")