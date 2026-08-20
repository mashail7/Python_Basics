money_for_the_day = float(input())
money_made_for_the_day = float(input())
money_to_spend = float(input())
money_needed = float(input())

total_money = ((money_for_the_day + money_made_for_the_day) * 5) - money_to_spend

if total_money >= money_needed:
    print(f"Profit: {total_money:.2f} BGN, the gift has been purchased.")
elif total_money < money_needed:
    money_insufficient = abs(total_money - money_needed)
    print(f"Insufficient money: {money_insufficient:.2f} BGN.")