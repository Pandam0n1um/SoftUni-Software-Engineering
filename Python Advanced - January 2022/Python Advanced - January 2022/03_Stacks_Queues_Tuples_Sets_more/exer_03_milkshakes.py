from collections import deque

chocolates = [int(choco) for choco in input().split(', ')]
cups_of_milk = deque([int(choco) for choco in input().split(', ')])
milkshakes = 0
while True:
	if not (chocolates and cups_of_milk):
		break
	curr_choco = chocolates.pop()
	curr_cup_of_milk = cups_of_milk.popleft()

	if curr_choco<=0 and curr_cup_of_milk<=0:
		continue
	if curr_choco<=0:
		cups_of_milk.appendleft(curr_cup_of_milk)
		continue
	if curr_cup_of_milk<=0:
		chocolates.append(curr_choco)
		continue

	if curr_choco == curr_cup_of_milk:
		milkshakes += 1
		if milkshakes == 5:
			break
	else:
		cups_of_milk.append(curr_cup_of_milk)
		if curr_choco > 5:
			chocolates.append(curr_choco - 5)

if milkshakes == 5:
	print("Great! You made all the chocolate milkshakes needed!")
else:
	print("Not enough milkshakes.")

if chocolates:
	print(f"Chocolate: ",end="")
	print(*chocolates, sep=', ')
else:
	print("Chocolate: empty")

if cups_of_milk:
	print(f"Milk: ",end="")
	print(*cups_of_milk, sep=', ')
else:
	print("Milk: empty")