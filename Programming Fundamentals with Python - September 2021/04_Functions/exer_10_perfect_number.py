import time

start = time.time()


def is_perfect_number(integer_number):
    halfsum = 0
    is_perfect = False
    for num in range(1, (integer_number//2)+1):
        if integer_number % num == 0:
            halfsum += num

    if halfsum == integer_number:
        is_perfect = True
    if is_perfect:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")
    return


int_number = int(input())

is_perfect_number(int_number)


end = time.time()

elapsed = end - start