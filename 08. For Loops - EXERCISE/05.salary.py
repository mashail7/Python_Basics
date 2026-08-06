opened_tabs = int(input())
salary = float(input())

for i in range(1, opened_tabs + 1, 1):
    tab = str(input())
    if tab == "Facebook":
        salary -= 150
    elif tab == "Instagram":
        salary -= 100
    elif tab == "Reddit":
        salary -= 50

if salary <= 0:
    print("You have lost your salary.")
else:
    print(f"{salary:.0f}")