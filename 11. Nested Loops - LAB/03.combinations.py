number = int(input())
valid_combinations = 0

for number1 in range(0 , number + 1):
    for number2 in range(0 ,number + 1):
        for number3 in range(0 ,number + 1):
            sum = number1 + number2 + number3
            if sum == number:
                valid_combinations += 1

print(valid_combinations)