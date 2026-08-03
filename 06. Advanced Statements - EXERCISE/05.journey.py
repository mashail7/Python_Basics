budget = float(input())
season = str(input())
destination = ""
place_to_live = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        budget = budget * 0.30
    elif season == "winter":
        budget = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        budget = budget * 0.40
    elif season == "winter":
        budget = budget * 0.80
elif budget > 1000:
    destination = "Europe"
    budget = budget * 0.90

if season == "summer" and destination != "Europe":
    place_to_live = "Camp"
elif season == "winter" or destination == "Europe":
    place_to_live = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place_to_live} - {budget:.02f}")
