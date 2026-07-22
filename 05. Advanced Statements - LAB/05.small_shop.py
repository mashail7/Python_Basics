product = str(input())
city = str(input())
quantity = float(input())

if product == "coffee":
    if city == "Sofia":
        total = quantity * 0.50
        print(total)
    elif city == "Plovdiv":
        total = quantity * 0.40
        print(total)
    elif city == "Varna":
        total = quantity * 0.45
        print(total)
elif product == "water":
    if city == "Sofia":
        total = quantity * 0.80
        print(total)
    elif city == "Plovdiv":
        total = quantity * 0.70
        print(total)
    elif city == "Varna":
        total = quantity * 0.70
        print(total)
elif product == "beer":
    if city == "Sofia":
        total = quantity * 1.20
        print(total)
    elif city == "Plovdiv":
        total = quantity * 1.15
        print(total)
    elif city == "Varna":
        total = quantity * 1.10
        print(total)
elif product == "sweets":
    if city == "Sofia":
        total = quantity * 1.45
        print(total)
    elif city == "Plovdiv":
        total = quantity * 1.30
        print(total)
    elif city == "Varna":
        total = quantity * 1.35
        print(total)
elif product == "peanuts":
    if city == "Sofia":
        total = quantity * 1.60
        print(total)
    elif city == "Plovdiv":
        total = quantity * 1.50
        print(total)
    elif city == "Varna":
        total = quantity * 1.55
        print(total)