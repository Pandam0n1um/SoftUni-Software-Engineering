from collections import deque

bomb_eff = deque([int(x) for x in input().split(', ')])
bomb_cast = [int(x) for x in input().split(', ')]


def mix_bomb(curr_bomb, curr_cast):
    while True:
        curr_mix = curr_bomb + curr_cast
        if curr_mix in bombs:
            bombs[curr_mix] += 1
            return
        elif curr_mix < 40:
            return
        else:
            curr_cast -= 5


is_enough = False
bombs = {
    60: 0,
    40: 0,
    120: 0
}
bombs_print = {
    60: 'Cherry Bombs',
    40: 'Datura Bombs',
    120: 'Smoke Decoy Bombs',
}

while True:
    if not (bomb_eff and bomb_cast):
        break
    curr_bomb = bomb_eff.popleft()
    curr_cast = bomb_cast.pop()
    mix_bomb(curr_bomb, curr_cast)

    if min(bombs.values()) >= 3:
        is_enough = True
        break

if is_enough:
    print('Bene! You have successfully filled the bomb pouch!')
else:
    print('You don\'t have enough materials to fill the bomb pouch.')

if bomb_eff:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_eff])}")
else:
    print('Bomb Effects: empty')

if bomb_cast:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_cast])}")
else:
    print("Bomb Casings: empty")

for el, count in bombs.items():
    print(f"{bombs_print[el]}: {count}")
