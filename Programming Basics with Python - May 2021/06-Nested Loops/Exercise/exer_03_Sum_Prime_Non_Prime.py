input_command = input()

prime_sum = 0
non_prime_sum = 0
is_negative = False

while not input_command == "stop":
    current_number = int(input_command)
    if current_number < 0:
        print("Number is negative.")
        input_command = input()
        continue

    counter_dividers = 0
    for i in range(1, current_number + 1):
        if current_number % i == 0:
            counter_dividers += 1
    if counter_dividers == 2:
        prime_sum += current_number
    else:
        non_prime_sum += current_number

    input_command = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
