name = str(input())
points_of_academy = float(input())
number_of_judges = int(input())
points = points_of_academy

for i in range(1, number_of_judges + 1):
    name_of_judge = str(input())
    points_given = float(input())
    points += points_given * ((len(name_of_judge)) / 2)

    if points >= 1250.5:
        print(f"Congratulations, {name} got a nominee for leading role with {points:.1f}!")
        break

if points < 1250.5:
    points_needed = 1250.5 - points
    print(f"Sorry, {name} you need {points_needed:.1f} more!")