width = int(input())
length = int(input())
height = int(input())

cubic_meters = width * length * height

while True:
    command = str(input())

    if command == "Done":
        print(f"{cubic_meters} Cubic meters left.")
        break

    box_amount = int(command)
    cubic_meters -= box_amount

    if cubic_meters <= 0:
        print(f"No more free space! You need {abs(cubic_meters)} Cubic meters more.")
        break