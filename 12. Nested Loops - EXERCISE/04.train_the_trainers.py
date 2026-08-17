n = int(input())
average_total = 0
count = 0

while True:
    presentation = input()
    if presentation == "Finish":
        break

    score = 0

    for i in range(1, n + 1):
        score += float(input())

    average_score = score / n

    print(f"{presentation} - {average_score:.2f}.")
    average_total += average_score
    count += 1

print(f"Student's final assessment is {(average_total / count):.2f}.")