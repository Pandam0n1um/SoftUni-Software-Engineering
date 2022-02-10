countries = input().split(", ")
capitals = input().split(", ")

count_cap = dict(zip(countries, capitals))

for country,capital in count_cap.items():
    print(f"{country} -> {capital}")