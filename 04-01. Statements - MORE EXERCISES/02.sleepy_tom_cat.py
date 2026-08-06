import math

WORK_DAY_PLAY = 63
OFF_DAY_PLAY = 127
NORM_FOR_PLAY = 30000

number_of_off_days = int(input())
number_of_work_days = 365 - number_of_off_days

minutes_of_play_for_year = (number_of_work_days * WORK_DAY_PLAY) + (number_of_off_days * OFF_DAY_PLAY)

if minutes_of_play_for_year > NORM_FOR_PLAY:
    difference_in_hours = math.floor(abs((NORM_FOR_PLAY - minutes_of_play_for_year)) / 60)
    difference_in_minutes = math.floor((minutes_of_play_for_year - NORM_FOR_PLAY) % 60)
    print("Tom will run away")
    print(f"{difference_in_hours:.00f} hours and {difference_in_minutes:.00f} minutes more for play")
elif minutes_of_play_for_year <= NORM_FOR_PLAY:
    difference_in_hours = math.floor(abs((NORM_FOR_PLAY - minutes_of_play_for_year)) / 60)
    difference_in_minutes = math.floor((NORM_FOR_PLAY - minutes_of_play_for_year) % 60)
    print("Tom sleeps well")
    print(f"{difference_in_hours:.00f} hours and {difference_in_minutes:.00f} minutes less for play")