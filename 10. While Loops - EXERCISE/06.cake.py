width = int(input())
height = int(input())
cake_pieces = width * height

while cake_pieces > 0:
    command = str(input())
    if command == "STOP":
        print(f"{cake_pieces} pieces are left.")
        break

    pieces_taken = int(command)
    cake_pieces -= pieces_taken

    if cake_pieces <= 0:
        print(f"No more cake left! You need {abs(cake_pieces)} pieces more.")
        break
