companies={}
while True:
    command = input()
    if command == "End":
        break
    company, employee = command.split(" -> ")
    if company not in companies:
        companies[company]=[]
    if employee not in companies[company]:
        companies[company].append(employee)

sorted_companies=dict(sorted(companies.items(), key=lambda x: x[0]))

for company,employee in sorted_companies.items():
    print(company)
    for employee in sorted_companies[company]:
        print(f"-- {employee}")
