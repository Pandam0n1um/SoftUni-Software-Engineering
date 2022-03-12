# from collections import deque
#
# fireworks = {'Palm': 0, 'Willow': 0, 'Crossette': 0}
#
# firework_eff = deque([int(x) for x in input().split(', ') if int(x)>0])
# explosive_power = [int(x) for x in input().split(', ')if int(x)>0]
#
# is_enough = False
#
#
# def create_firework(curr_eff, curr_power):
#     total_sum = curr_eff + curr_power
#     divisible_three = (total_sum % 3 == 0)
#     divisible_five = (total_sum % 5 == 0)
#     if divisible_three and not divisible_five:
#         fireworks['Palm'] += 1
#         return True
#     elif not divisible_three and divisible_five:
#         fireworks['Willow'] += 1
#         return True
#     elif divisible_three and divisible_five:
#         fireworks['Crossette'] += 1
#         return True
#     else:
#         return False
#
#
# while True:
#     if not (firework_eff and explosive_power):
#         break
#     curr_eff = firework_eff.popleft()
#     curr_power = explosive_power.pop()
#     creation_result = create_firework(curr_eff, curr_power)
#     if min(fireworks.values()) >= 3:
#         is_enough = True
#         break
#     if not creation_result:
#         if curr_eff>1:
#             firework_eff.append(curr_eff - 1)
#         explosive_power.append(curr_power)
#
#
# if is_enough:
#     print('Congrats! You made the perfect firework show!')
# else:
#     print('Sorry. You can\'t make the perfect firework show.')
#
# if firework_eff:
#     print(f"Firework Effects left: {', '.join(str(eff) for eff in firework_eff)}")
# if explosive_power:
#     print(f"Explosive Power left: {', '.join(str(expl) for expl in explosive_power)}")
# for firework, count in fireworks.items():
#     print(f"{firework} Fireworks: {count}")


from collections import deque

fireworks = deque(int(x) for x in input().split(', ') if int(x) > 0)
explosive_powers = [int(x) for x in input().split(', ') if int(x) > 0]

mixed_fireworks = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0
}

successful = False

while fireworks and explosive_powers:
    firework = fireworks[0]
    power = explosive_powers[-1]
    result = firework + power
    if result % 3 == 0 and result % 5 != 0:
        mixed_fireworks['Palm Fireworks'] += 1
        fireworks.popleft()
        explosive_powers.pop()
    elif result % 5 == 0 and result % 3 != 0:
        mixed_fireworks['Willow Fireworks'] += 1
        fireworks.popleft()
        explosive_powers.pop()
    elif result % 3 == 0 and result % 5 == 0:
        mixed_fireworks['Crossette Fireworks'] += 1
        fireworks.popleft()
        explosive_powers.pop()
    else:
        if fireworks[0]>1:
            fireworks[0] -= 1
            fireworks.append(fireworks.popleft())
        else:
            fireworks.popleft()
    if mixed_fireworks['Palm Fireworks'] >= 3 and mixed_fireworks['Willow Fireworks'] >= 3 and mixed_fireworks[
        "Crossette Fireworks"] >= 3:
        successful = True
        break

if successful:
    print('Congrats! You made the perfect firework show!')
else:
    print("Sorry. You can't make the perfect firework show.")
if fireworks:
    print(f'Firework Effects left: {", ".join(str(x) for x in fireworks)}')
if explosive_powers:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_powers)}")
for explosive, count in mixed_fireworks.items():
    print(f'{explosive}: {count}')