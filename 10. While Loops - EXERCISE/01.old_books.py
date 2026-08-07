book = str(input())
counter = 0
book_found = False

while not book_found:
    book_checked = str(input())

    if book_checked == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {counter} books.")
        break

    if book_checked == book:
        book_found = True
        print(f"You checked {counter} books and found it.")
    else:
        counter += 1