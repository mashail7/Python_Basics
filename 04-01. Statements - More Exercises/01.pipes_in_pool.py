v = int(input())
p1 = int(input())
p2 = int(input())
hours = float(input())

total_water_for_hours = (p1 + p2) * hours

if total_water_for_hours > v:
    water_left = total_water_for_hours - v
    print(f"For {hours:.02f} hours the pool overflows with {water_left:.02f} liters.")
elif total_water_for_hours <= v:
    percent_water_from_p1 = (((p1 * hours) / total_water_for_hours) * 100)
    percent_water_from_p2 = (((p2 * hours) / total_water_for_hours) * 100)
    percent_water_in_pool = ((total_water_for_hours / v) * 100)
    print(f"The pool is {percent_water_in_pool:.02f}% full. Pipe 1: {percent_water_from_p1:.02f}%. Pipe 2: {percent_water_from_p2:.02f}%.")