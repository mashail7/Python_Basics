number_of_groups = int(input())
amount_of_people = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1, number_of_groups + 1):
    number_of_people = int(input())
    amount_of_people += number_of_people
    if number_of_people <= 5:
        p1 += number_of_people
    elif 6 <= number_of_people <= 12:
        p2 += number_of_people
    elif 13 <= number_of_people <= 25:
        p3 += number_of_people
    elif 26 <= number_of_people <= 40:
        p4 += number_of_people
    elif number_of_people > 40:
        p5 += number_of_people

print(f"{((p1 / amount_of_people) * 100):.2f}%")
print(f"{((p2 / amount_of_people) * 100):.2f}%")
print(f"{((p3 / amount_of_people) * 100):.2f}%")
print(f"{((p4 / amount_of_people) * 100):.2f}%")
print(f"{((p5 / amount_of_people) * 100):.2f}%")