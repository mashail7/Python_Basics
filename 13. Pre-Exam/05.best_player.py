most_goals = 0
best_player = ""

while True:
    command = input()
    if command == "END":
        print(f"{best_player} is the best player!")
        if most_goals >= 3:
            print(f"He has scored {most_goals} goals and made a hat-trick !!!")
        else:
            print(f"He has scored {most_goals} goals.")
        break

    goals = int(input())

    if goals > most_goals:
        best_player = command
        most_goals = goals

    if most_goals >= 10:
        print(f"{best_player} is the best player!")
        print(f"He has scored {most_goals} goals and made a hat-trick !!!")
        break

