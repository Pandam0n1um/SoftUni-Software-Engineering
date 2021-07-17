bottles_count = int(input())
detergent_amount = 750 * bottles_count
is_detergent_left = False
cycle_counter = 0
plates_counter = 0
pots_counter = 0

while 0 <= detergent_amount:
    line_input = str(input())
    if line_input == "End":
        is_detergent_left = True
        break
    cycle_counter += 1
    line_input=int(line_input)
    if cycle_counter % 3 == 0:
        detergent_amount -= (line_input * 15)
        pots_counter += line_input
    else:
        detergent_amount -= (line_input * 5)
        plates_counter += line_input

if is_detergent_left:
    print(f"Detergent was enough!")
    print(f"{plates_counter} dishes and {pots_counter} pots were washed.")
    print(f"Leftover detergent {detergent_amount} ml.")
else:
    print(f"Not enough detergent, {abs(detergent_amount)} ml. more necessary!")