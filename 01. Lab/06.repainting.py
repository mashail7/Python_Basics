PROTECTIVE_PLASTIC_PRICE = 1.50
PAINT_PRICE = 14.50
PAINT_THINNER_PRICE = 5

EXTRA_PAINT = 0.10
EXTRA_PROTECTIVE_PLASTIC = 2
BAGS = 0.40
LABOR = 0.30

protective_plastic_amount = int(input())
paint_amount = int(input())
thinner_amount = int(input())
hours_of_labor = int(input())

total_plastic = (protective_plastic_amount + EXTRA_PROTECTIVE_PLASTIC) * PROTECTIVE_PLASTIC_PRICE
total_paint = (paint_amount + (paint_amount * EXTRA_PAINT)) * PAINT_PRICE
total_thinner = thinner_amount * PAINT_THINNER_PRICE

total_for_materials = total_plastic + total_paint + total_thinner + BAGS
total_labor = (total_for_materials * LABOR) * hours_of_labor
total = total_for_materials + total_labor

print(total)