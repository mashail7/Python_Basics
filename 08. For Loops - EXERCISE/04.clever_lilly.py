age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

EVEN_BIRTHDAY_GIFT = 10
BROTHER_STEAL = 1
total = 0
toys_amount = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        total += (EVEN_BIRTHDAY_GIFT * (year / 2) - BROTHER_STEAL)
    else:
        toys_amount += 1

total += (toys_amount * toy_price)

if total >= washing_machine_price:
    money_left = total - washing_machine_price
    print(f"Yes! {money_left:.2f}")
elif total < washing_machine_price:
    money_needed = washing_machine_price - total
    print(f"No! {money_needed:.2f}")