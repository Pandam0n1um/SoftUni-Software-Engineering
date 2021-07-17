total_steps = 0
steps_left = 10000

while total_steps < steps_left:
    input_command = str(input())
    if input_command == str("Going home"):
        input_command=int(input())
        total_steps+=input_command
        break
    else:
        steps_walked = int(input_command)
        total_steps += steps_walked

distance_difference = abs(total_steps - steps_left)

if total_steps < steps_left:
    print(f"{distance_difference} more steps to reach goal.")
else:
    print(f"Goal reached! Good job!")
    print(f"{distance_difference} steps over the goal!")
