import math

days = int(input())
food_left_in_kg = int(input())
dog_food_left_in_kg = float(input())
cat_food_left_in_kg = float(input())
turtle_food_left_in_g = float(input())

dog_food_total = dog_food_left_in_kg * days
cat_food_total = cat_food_left_in_kg * days
turtle_food_total = (turtle_food_left_in_g * days) / 1000

total_food_needed = dog_food_total + cat_food_total + turtle_food_total

if food_left_in_kg >= total_food_needed:
    food_left_in_kg -= total_food_needed
    print(f"{math.floor(food_left_in_kg)} kilos of food left.")
elif food_left_in_kg < total_food_needed:
    total_food_needed -= food_left_in_kg
    print(f"{math.ceil(total_food_needed)} more kilos of food are needed.")