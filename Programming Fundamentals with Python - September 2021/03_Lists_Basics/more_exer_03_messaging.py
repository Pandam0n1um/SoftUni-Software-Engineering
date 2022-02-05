number_sequence = input().split()
chars_sequence = input()

result = ""

for index in range(len(number_sequence)):
    length = len(chars_sequence)
    number = number_sequence[index]
    summation = sum(map(int, str(number)))
    if summation>length-1:
        position = (summation // length)
        summation=position
    result += chars_sequence[summation]
    chars_sequence=chars_sequence[:summation]+chars_sequence[summation+1:]

print(result)
