import math

serial = input("")
episode_time = int(input())
break_time = int(input())

lunch_time = break_time / 8
chill_time = break_time / 4

break_time_left = break_time - (lunch_time + chill_time)

if break_time_left >= episode_time:
    time_left = break_time_left - episode_time
    print(f"You have enough time to watch {serial} and left with {math.ceil(time_left)} minutes free time.")
elif break_time_left < episode_time:
    time_needed = abs(break_time_left - episode_time)
    print(f"You don't have enough time to watch {serial}, you need {math.ceil(time_needed)} more minutes.")