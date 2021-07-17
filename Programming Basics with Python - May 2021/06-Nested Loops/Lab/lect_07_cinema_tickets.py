movie_title = str(input())

student_tickets = 0
standard_tickets = 0
kid_tickets = 0
total_tickets = 0

while not movie_title == "Finish":
    current_movie_tickets = 0
    free_seats = int(input())
    while free_seats > current_movie_tickets:
        ticket_type = str(input())
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
        elif ticket_type == "End":
            break
        total_tickets += 1
        current_movie_tickets += 1
    current_tickets_ratio = (current_movie_tickets / free_seats) * 100
    print(f"{movie_title} - {current_tickets_ratio:.2f}% full.")
    movie_title = str(input())

student_tickets_ratio = (student_tickets / total_tickets) * 100
standard_tickets_ratio = (standard_tickets / total_tickets) * 100
kid_tickets_ratio = (kid_tickets / total_tickets) * 100

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets_ratio:.2f}% student tickets.")
print(f"{standard_tickets_ratio:.2f}% standard tickets.")
print(f"{kid_tickets_ratio:.2f}% kids tickets.")
