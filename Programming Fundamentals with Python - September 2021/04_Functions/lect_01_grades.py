# def grade_to_text(grade):
#     if 2 <= grade <= 2.99:
#         return "Fail"
#     elif 2 <= grade <= 2.99:
#         return "Fail"
#     elif 3 <= grade <= 3.49:
#         return "Poor"
#     elif 3.50 <= grade <= 4.49:
#         return "Good"
#     elif 4.50 <= grade <= 5.49:
#         return "Very Good"
#     elif 5.50 <= grade <= 6.00:
#         return "Excellent"
#
#
# grade_as_float = float(input())
# print(grade_to_text(grade_as_float))


def data_type(command):
    if command == 'int':
        return int(data) * 2
    elif command == 'real':
        return f'{(int(data) * 1.5):.2f}'
    elif command == 'string':
        return f'${data}$'


string = input()
data = input()
print(data_type(string))