amount_required = int(input())

amount_gathered = 0
transaction_counter = 0

is_money_gathered = True
is_transaction_failed = True

total_cs = 0
total_cc = 0
counter_cs = 0
counter_cc = 0
average_cs = 0
average_cc = 0

while amount_gathered < amount_required:
    transaction_counter += 1
    line_input = str(input())
    if line_input == "End":
        is_money_gathered = False
        break
    product_cost = int(line_input)
    transaction_odd_even = transaction_counter % 2

    if transaction_odd_even == 0 and product_cost >= 10:
        counter_cc += 1
        total_cc += product_cost
        is_transaction_failed = False
        average_cc = total_cc / counter_cc
    elif transaction_odd_even == 1 and product_cost <= 100:
        counter_cs += 1
        total_cs += product_cost
        is_transaction_failed = False
        average_cs = total_cs / counter_cs
    else:
        is_transaction_failed = True

    if is_transaction_failed:
        print(f"Error in transaction!")
    else:
        amount_gathered += product_cost
        print(f"Product sold!")

if not is_money_gathered:
    print(f"Failed to collect required money for charity.")
else:
    print(f"Average CS: {average_cs:.2f}")
    print(f"Average CC: {average_cc:.2f}")
