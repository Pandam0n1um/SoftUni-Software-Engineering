# word = str(input())
# sum_letter = 0
#
# for letter in word:
#     if letter == "a":
#         sum_letter += 1
#     elif letter == "e":
#         sum_letter += 2
#     elif letter == "i":
#         sum_letter += 3
#     elif letter == "o":
#         sum_letter += 4
#     elif letter == "u":
#         sum_letter += 5
#
# print(sum_letter)

word = str(input())
sum_letter = 0

for index in range(0, len(word)):
    if word[index] == "a":
        sum_letter += 1
    elif word[index] == "e":
        sum_letter += 2
    elif word[index] == "i":
        sum_letter += 3
    elif word[index] == "o":
        sum_letter += 4
    elif word[index] == "u":
        sum_letter += 5

print(sum_letter)
