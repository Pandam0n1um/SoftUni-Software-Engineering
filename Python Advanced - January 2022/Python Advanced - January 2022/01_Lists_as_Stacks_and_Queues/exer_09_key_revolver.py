from collections import deque

bullet_price = int(input())
gun_barrel = int(input())
bullets = deque([int(el) for el in input().split()])
locks = deque([int(el) for el in input().split()])
value = int(input())

counter = 0
is_open = False
total_bullets=len(bullets)

for bullet in range(total_bullets):
    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    counter += 1
    if current_lock >= current_bullet:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(current_lock)
    value -= bullet_price
    if counter % gun_barrel == 0 and counter < total_bullets:
        print("Reloading!")
    if len(locks) == 0:
        is_open = True
        break
bullets_left = total_bullets - counter
if is_open:
    print(f"{bullets_left} bullets left. Earned ${value}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")