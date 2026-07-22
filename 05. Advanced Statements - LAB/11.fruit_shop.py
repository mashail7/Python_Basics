fruit = str(input())
day = str(input())
quantity = float(input())

total = 0

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        total = quantity * 2.50
    elif fruit == "apple":
        total = quantity * 1.20
    elif fruit == "orange":
        total = quantity * 0.85
    elif fruit == "grapefruit":
        total = quantity * 1.45
    elif fruit == "kiwi":
        total = quantity * 2.70
    elif fruit == "pineapple":
        total = quantity * 5.50
    elif fruit == "grapes":
        total = quantity * 3.85
    else:
        print("error")
elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        total = quantity * 2.70
    elif fruit == "apple":
        total = quantity * 1.25
    elif fruit == "orange":
        total = quantity * 0.90
    elif fruit == "grapefruit":
        total = quantity * 1.60
    elif fruit == "kiwi":
        total = quantity * 3.00
    elif fruit == "pineapple":
        total = quantity * 5.60
    elif fruit == "grapes":
        total = quantity * 4.20
    else:
        print("error")
else:
    print("error")

if total != 0:
    print(f"{total:.02f}")