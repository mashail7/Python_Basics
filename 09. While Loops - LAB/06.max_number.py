import sys
max_number = -sys.maxsize

while True:
    command = input()
    if command == "Stop":
        break
    else:
        number = int(command)
        if number > max_number:
            max_number = number

print(max_number)