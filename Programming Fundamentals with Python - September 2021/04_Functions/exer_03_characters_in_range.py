def character_range(char_1, char_2):
    start = ord(char_1)
    end = ord(char_2)

    result = []
    for value in range(start+1, end):
        result.append(chr(value))
    result_str = ' '.join([str(elem) for elem in result])
    return result_str


character_1 = input()
character_2 = input()

print_value=character_range(character_1, character_2)
print(print_value)
