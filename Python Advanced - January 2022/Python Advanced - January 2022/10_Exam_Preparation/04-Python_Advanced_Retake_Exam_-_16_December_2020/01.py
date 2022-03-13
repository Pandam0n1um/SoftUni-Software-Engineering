from collections import deque

males = [int(x) for x in input().split() if int(x) > 0]
females = deque([int(x) for x in input().split() if int(x) > 0])


def match_pair(curr_male, curr_female):
    if curr_male == curr_female:
        return 'Match'
    else:
        return 'Mismatch'


matches = 0

while True:
    if not (males and females):
        break
    curr_male = males.pop()
    curr_female = females.popleft()
    counter_male = 0
    counter_female = 0
    if curr_male % 25 == 0:
        while males:
            if counter_male == 1:
                break
            males.pop()
            counter_male += 1
    if curr_female % 25 == 0:
        while females:
            if counter_female == 1:
                break
            females.pop()
            counter_female += 1
    result = match_pair(curr_male, curr_female)
    if result == 'Mismatch' and curr_male - 2 > 0:
        males.append(curr_male - 2)
    elif result == 'Match':
        matches += 1
# print(males)
# print(females)
print(f"Matches: {matches}")
males = males[::-1]
if males:
    print(f"Males left: {', '.join(str(man) for man in males)}")
    print("Females left: none")
else:
    print("Males left: none")
    print(f"Females left: {', '.join(str(woman) for woman in females)}")
