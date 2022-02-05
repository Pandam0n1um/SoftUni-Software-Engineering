def add_and_subtract():
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())

    def sum_numbers():
        return num_1 + num_2

    def subtract():
        return sum_numbers() - num_3

    result = subtract()
    return result


a = add_and_subtract()

print(a)