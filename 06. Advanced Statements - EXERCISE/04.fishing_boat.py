budget = int(input())
season = str(input())
people = int(input())

total = 0

if season == "Spring":
    total = 3000
elif season == "Summer" or season == "Autumn":
    total = 4200
elif season == "Winter":
    total = 2600

if people <= 6:
    total = total * 0.90
elif 7 <= people <= 11:
    total = total * 0.85
elif people >= 12:
    total = total * 0.75

if people % 2 == 0 and season != "Autumn":
    total = total * 0.95

if budget >= total:
    money_left = budget - total
    print(f"Yes! You have {money_left:.02f} leva left.")
elif budget < total:
    money_needed = total - budget
    print(f"Not enough money! You need {money_needed:.02f} leva.")