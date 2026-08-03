degrees = int(input())
time_of_day = str(input())

if 10 <= degrees <= 18:
    if time_of_day == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    elif time_of_day == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    elif time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

elif 18 < degrees <= 24:
    if time_of_day == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    elif time_of_day == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    elif time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

elif degrees >= 25:
    if time_of_day == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    elif time_of_day == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    elif time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")