student = 0
standard = 0
kid = 0
total_tickets = 0

while True:
    film = input()
    if film == "Finish":
        break

    current_free_seats = 0

    free_seats = int(input())

    for seat in range(free_seats):
        type_of_seat = input()
        if type_of_seat == "End":
            break

        total_tickets += 1
        current_free_seats += 1

        if type_of_seat == "student":
            student += 1
        elif type_of_seat == "standard":
            standard += 1
        elif type_of_seat == "kid":
            kid += 1

    print(f"{film} - {((current_free_seats / free_seats) * 100):.2f}% full.")

print(f"Total tickets: {total_tickets}")
print(f"{((student / total_tickets) * 100):.2f}% student tickets.")
print(f"{((standard / total_tickets) * 100):.2f}% standard tickets.")
print(f"{((kid / total_tickets) * 100):.2f}% kids tickets.")
