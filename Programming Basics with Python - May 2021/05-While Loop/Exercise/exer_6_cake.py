cake_width = int(input())
cake_length = int(input())
cake_size = cake_length * cake_width
is_cake_left=False

while 0<=cake_size:
    operation_input=str(input())
    if operation_input=="STOP":
        is_cake_left=True
        break
    pieces_taken=int(operation_input)
    cake_size-=pieces_taken

if is_cake_left:
    print(f"{cake_size} pieces are left.")
else:
    print(f"No more cake left! You need {abs(cake_size)} pieces more.")