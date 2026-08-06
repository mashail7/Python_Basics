import sys
min_number = sys.maxsize

while True:
    command = input()
    if command == "Stop":
        break
    else:
        number = int(command)
        if number < min_number:
            min_number = number

print(min_number)