budget_movie = float(input())
number_statists = int(input())
clothes_price_per_statists = float(input())

decor = budget_movie * 0.10

if number_statists > 150:
    clothes_price_per_statists = clothes_price_per_statists * 0.90

clothes_total = clothes_price_per_statists * number_statists
total_price = decor + clothes_total

if total_price > budget_movie:
    money_needed = total_price - budget_movie
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.02f} leva more.")
elif total_price <= budget_movie:
    money_left = budget_movie - total_price
    print("Action!")
    print(f"Wingard starts filming with {money_left:.02f} leva left.")