money_needed_for_vacation = float(input())
money_saved = float(input())
spend_streak = 0
days= 0

while True:
    spend_or_save = str(input())
    money_for_the_day = float(input())

    if spend_or_save == "spend":
        spend_streak += 1
        days += 1
        if spend_streak >= 5:
            print("You can't save the money.")
            print(f"{days}")
            break
        if money_for_the_day >= money_saved:
            money_saved = 0
        else:
            money_saved -= money_for_the_day
    elif spend_or_save == "save":
        spend_streak = 0
        money_saved += money_for_the_day
        days += 1
        if money_saved >= money_needed_for_vacation:
            print(f"You saved the money for {days} days.")
            break
