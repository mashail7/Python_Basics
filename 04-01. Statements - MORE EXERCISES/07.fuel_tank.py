fuel_type = input("")
fuel_left = float(input())

if fuel_type == "Diesel":
    if fuel_left >= 25:
        print(f"You have enough diesel.")
    elif fuel_left < 25:
        print(f"Fill your tank with diesel!")
elif fuel_type == "Gasoline":
    if fuel_left >= 25:
        print(f"You have enough gasoline.")
    elif fuel_left < 25:
        print(f"Fill your tank with gasoline!")
elif fuel_type == "Gas":
    if fuel_left >= 25:
        print(f"You have enough gas.")
    elif fuel_left < 25:
        print(f"Fill your tank with gas!")
else:
    print("Invalid fuel!")