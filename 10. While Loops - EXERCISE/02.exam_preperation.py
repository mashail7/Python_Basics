bad_grades_limit = int(input())
number_of_exams = 0
score_total = 0
bad_grades = 0
last_exam = ""

while True:
    exam = str(input())

    if exam == "Enough":
        print(f"Average score: {(score_total / number_of_exams):.2f}")
        print(f"Number of problems: {number_of_exams}")
        print(f"Last problem: {last_exam}")
        break

    grade = int(input())

    if grade <= 4:
        bad_grades += 1
        number_of_exams += 1
        score_total += grade
        last_exam = exam
        if bad_grades >= bad_grades_limit:
            print(f"You need a break, {bad_grades} poor grades.")
            break
    else:
        number_of_exams += 1
        score_total += grade
        last_exam = exam