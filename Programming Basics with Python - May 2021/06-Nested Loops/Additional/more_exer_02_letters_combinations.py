first_letter = input()
second_letter = input()
third_letter = input()
counter_valid_comb=0
for letter_1 in range(ord(first_letter), ord(second_letter)+1):
    is_ommited_1 = False
    if letter_1 == ord(third_letter):
        is_ommited_1 = True
    for letter_2 in range(ord(first_letter), ord(second_letter)+1):
        is_ommited_2 = False
        if letter_2 == ord(third_letter):
            is_ommited_2 = True
        for letter_3 in range(ord(first_letter), ord(second_letter)+1):
            is_ommited_3 = False
            if letter_3 == ord(third_letter):
                is_ommited_3 = True
            if (not is_ommited_3) and (not is_ommited_2) and (not is_ommited_1):
                counter_valid_comb +=1
                print(f"{chr(letter_1)}{chr(letter_2)}{chr(letter_3)}",end=" ")
print(counter_valid_comb)