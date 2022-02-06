input_list = input().split()

searched_palindrome = input()

palindromes = []

searched_palindrome_counter = 0

for current_element in input_list:
    if current_element == current_element[::-1]:
        palindromes.append(current_element)

    if current_element == searched_palindrome:
        searched_palindrome_counter += 1

print(palindromes)
print(f"Found palindrome {searched_palindrome_counter} times")
