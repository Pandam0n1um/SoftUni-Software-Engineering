from collections import deque


def calculate(curr_iter):
    curr_total = sum([idx * val for idx, val in enumerate(curr_iter)])
    return curr_total


def best_list_pureness(numbers, k):
    k=min(k,len(numbers))
    numbers = deque(numbers)
    result = {}
    for step in range(k+1):
        curr_result = calculate(numbers)
        result[step] = curr_result
        numbers.rotate(1)
    result_sorted = sorted(result.items(), key=lambda x: (-x[1], x[0]))
    return f"Best pureness {result_sorted[0][1]} after {result_sorted[0][0]} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
