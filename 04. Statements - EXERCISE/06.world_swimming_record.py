import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_to_swim_1_meter = float(input())

total_time_to_swim = time_in_seconds_to_swim_1_meter * distance_in_meters

resistance_times = math.floor(distance_in_meters / 15)
resistance_total_seconds = resistance_times * 12.5

total_time_to_swim = total_time_to_swim + resistance_total_seconds

if total_time_to_swim < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time_to_swim:.02f} seconds.")
elif total_time_to_swim >= record_in_seconds:
    seconds_needed = record_in_seconds - total_time_to_swim
    print(f"No, he failed! He was {abs(seconds_needed):.02f} seconds slower.")