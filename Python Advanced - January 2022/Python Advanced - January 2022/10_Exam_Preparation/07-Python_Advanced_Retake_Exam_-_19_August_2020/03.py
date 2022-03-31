def list_manipulator(numbers, *args):
    action = args[0]
    location = args[1]
    if action == 'add':
        rest = list(args[2:])
        numbers = numbers + rest if location == 'end' else rest + numbers
    else:
        pos = args[-1] if type(args[-1]) == int else 1
        numbers = numbers[pos:] if location == 'beginning' else numbers[:-pos]
    return numbers


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
