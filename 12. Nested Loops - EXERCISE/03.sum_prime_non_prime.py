prime_number_sum = 0
non_prime_number_sum = 0


while True:
    command = input()
    if command == "stop":
        break

    number = int(command)
    is_prime = False
    is_non_prime = False

    if number == 0 or number == 1:
        non_prime_number_sum += number
        continue
    elif number == 2:
        prime_number_sum += number
        continue

    if number >= 0:
        for i in range(2, number):
            if number % i == 0:
                is_non_prime = True
                is_prime = False
                break
            else:
                is_prime = True
    else:
        print("Number is negative.")
        continue

    if is_prime:
        prime_number_sum += number
    elif is_non_prime:
        non_prime_number_sum += number

print(f"Sum of all prime numbers is: {prime_number_sum}")
print(f"Sum of all non prime numbers is: {non_prime_number_sum}")