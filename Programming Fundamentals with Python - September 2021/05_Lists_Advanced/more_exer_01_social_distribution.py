from decimal import Decimal


def max_min_redistribution(wlth_List):
    max_value = max(wlth_List)
    min_value = min(wlth_List)
    max_value_index = wlth_List.index(max_value)
    min_value_index = wlth_List.index(min_value)
    redistribution = 0
    if max_value - min_value >= minimum_wealth:
        redistribution = minimum_wealth - min_value
    else:
        redistribution = max_value - minimum_wealth
    wlth_List[max_value_index] -= redistribution
    wlth_List[min_value_index] += redistribution

    return wlth_List


wealth_list = [int(i) for i in input().split(", ")]

minimum_wealth = int(input())

total_wealth = sum(wealth_list)

average_wealth = total_wealth / len(wealth_list)

if Decimal(average_wealth) < Decimal(minimum_wealth):
    print("No equal distribution possible")
    exit()
else:
    while True:
        if min(wealth_list) >= minimum_wealth:
            break
        else:
            wealth_list = max_min_redistribution(wealth_list)

print(wealth_list)
