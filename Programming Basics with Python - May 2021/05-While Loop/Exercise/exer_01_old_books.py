book_to_find = str(input())

books_counter = 0
is_book_found=False

current_book=str(input())

while not (current_book == str("No More Books")):
    if current_book == book_to_find:
        is_book_found=True
        print(f"You checked {books_counter} books and found it.")
        break
    books_counter += 1
    current_book = str(input())

if not is_book_found:
    print(f"The book you search is not here!")
    print(f"You checked {books_counter} books.")
