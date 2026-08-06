name = str(input())
counter = 0
fail_counter = 0
sum_of_grades = 0

while True:
    grade = float(input())

    if fail_counter == 1 and grade < 4:
        print(f"{name} has been excluded at {counter + 1} grade")
        break

    if grade < 4:
        fail_counter += 1
    else:
        sum_of_grades += grade
        counter += 1

    if counter == 12:
        print(f"{name} graduated. Average grade: {(sum_of_grades / counter):.2f}")
        break