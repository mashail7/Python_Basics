STEPS_GOAL = 10000
steps_today = 0

while True:
    command = str(input())
    if command == "Going home":
        steps_to_home = int(input())
        steps_today += steps_to_home
        if steps_today < STEPS_GOAL:
            print(f"{STEPS_GOAL - steps_today} more steps to reach goal.")
            break
        else:
            print("Goal reached! Good job!")
            print(f"{steps_today - STEPS_GOAL} steps over the goal!")
            break

    steps_made = int(command)
    steps_today += steps_made

    if steps_today >= STEPS_GOAL:
        difference = steps_today - STEPS_GOAL
        print("Goal reached! Good job!")
        print(f"{difference} steps over the goal!")
        break