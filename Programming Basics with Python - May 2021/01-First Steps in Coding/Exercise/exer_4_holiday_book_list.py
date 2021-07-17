book_page_count = int(input())

hourly_page_count = int(input())

days_per_book=int(input())

hours_per_book=float(book_page_count/hourly_page_count)

hours_per_day=float(hours_per_book/days_per_book)

print(hours_per_day)