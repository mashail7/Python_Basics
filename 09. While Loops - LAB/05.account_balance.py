total = 0

while True:
    command = input()
    if command == "NoMoreMoney":
        break

    money_to_increase = float(command)

    if money_to_increase < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {money_to_increase:.2f}")
        total += money_to_increase

print(f"Total: {total:.2f}")