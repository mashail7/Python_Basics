ROSE = 5
DAHLIA = 3.80
TULIP = 2.80
NARCISSUS = 3
GLADIOLA = 2.50

flower = str(input())
amount = int(input())
budget = int(input())
total = 0

if flower == "Roses":
    if amount > 80:
        total = (amount * ROSE) * 0.90
    else:
        total = (amount * ROSE)
elif flower == "Dahlias":
    if amount > 90:
        total = (amount * DAHLIA) * 0.85
    else:
        total = (amount * DAHLIA)
elif flower == "Tulips":
    if amount > 80:
        total = (amount * TULIP) * 0.85
    else:
        total = (amount * TULIP)
elif flower == "Narcissus":
    if amount < 120:
        total = (amount * NARCISSUS) * 1.15
    else:
        total = (amount * NARCISSUS)
elif flower == "Gladiolus":
    if amount < 80:
        total = (amount * GLADIOLA) * 1.20
    else:
        total = (amount * GLADIOLA)

if budget >= total:
    money_left = budget - total
    print(f"Hey, you have a great garden with {amount} {flower} and {money_left:.02f} leva left.")
elif budget < total:
    money_needed = total - budget
    print(f"Not enough money, you need {money_needed:.02f} leva more.")