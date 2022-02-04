wolf_sheep_queue_input = input()

wolf_sheep_queue = wolf_sheep_queue_input.split(", ")

if wolf_sheep_queue[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for index in range(0, len(wolf_sheep_queue)):
        if wolf_sheep_queue[-(index + 1)] == "wolf":
            print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")

