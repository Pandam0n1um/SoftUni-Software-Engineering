space_width = int(input())
space_length = int(input())
space_height = int(input())

volume_total = space_width * space_length * space_height
volume_left = volume_total

while volume_left >= 0:
    new_input = str(input())
    if new_input != str("Done"):
        new_crates = int(new_input)
        volume_left -= new_crates

    else:
        break

if volume_left>0:
    print(f"{abs(volume_left)} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(volume_left)} Cubic meters more.")