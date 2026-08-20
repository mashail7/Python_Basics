PAPER = 5.80
LEATHER = 7.20
GLUE = 1.20

paper = int(input())
leather = int(input())
glue = float(input())
discount = int(input())

total_paper = paper * PAPER
total_leather = leather * LEATHER
total_glue = glue * GLUE

total_without_discount = total_paper + total_leather + total_glue
total = total_without_discount - (total_without_discount * (discount / 100))

print(f"{total:.3f}")