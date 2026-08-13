total_money_got = 0

while True:
    command = input()

    if command == "End":
        break

    money_needed = float(input())

    while total_money_got < money_needed:
        money_got = float(input())
        total_money_got += money_got
        if total_money_got >= money_needed:
            print(f"Going to {command}!")
            total_money_got = 0
            break
