import math

shape = input()

if shape == "square":
    side = float(input())
    print(f"{side * side:.3f}")
elif shape == "rectangle":
    side_1 = float(input())
    side_2 = float(input())
    print(f"{side_1 * side_2:.3f}")
elif shape == "circle":
    side = float(input())
    print(f"{(side * side) * math.pi:.3f}")
elif shape == "triangle":
    side_1 = float(input())
    side_2 = float(input())
    print(f"{(side_1 * side_2) / 2:.3f}")