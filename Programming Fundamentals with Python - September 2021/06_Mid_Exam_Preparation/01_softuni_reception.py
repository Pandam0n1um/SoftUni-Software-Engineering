empl_1_rate = int(input())
empl_2_rate = int(input())
empl_3_rate = int(input())

students_count = int(input())

service_rate = empl_1_rate + empl_2_rate + empl_3_rate
counter = 0
hours = 0
while True:
    if students_count <= 0:
        break
    if not counter == 0 and counter % 3 == 0:
        hours += 1
    counter += 1
    hours += 1
    students_count -= service_rate

print(f"Time needed: {hours}h.")
