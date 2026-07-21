import math

cubic_meters_vineyard = int(input())
grape_per_cubic_meter = float(input())
liters_vine_needed = int(input())
number_of_workers = int(input())

forty_percent_of_harvest = (cubic_meters_vineyard * grape_per_cubic_meter) * 0.40
cubic_meters_vineyard -= forty_percent_of_harvest

liters_vine_made = forty_percent_of_harvest / 2.5

if liters_vine_made < liters_vine_needed:
    vine_needed = math.floor(liters_vine_needed - liters_vine_made)
    print(f"It will be a tough winter! More {vine_needed} liters wine needed.")
elif liters_vine_made >= liters_vine_needed:
    vine_left = math.ceil(liters_vine_made - liters_vine_needed)
    vine_per_worker = math.ceil(vine_left / number_of_workers)
    print(f"Good harvest this year! Total wine: {math.floor(liters_vine_made)} liters.")
    print(f"{vine_left} liters left -> {vine_per_worker} liters per person.")
