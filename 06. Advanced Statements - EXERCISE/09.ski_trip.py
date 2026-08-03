days = int(input())
room_type = str(input())
rate = str(input())

price_for_hotel = 0

if room_type == "room for one person":
    price_for_hotel = (days - 1) * 18
elif room_type == "apartment":
    if days < 10:
        price_for_hotel = ((days - 1) * 25) * 0.70
    elif 10 <= days <= 15:
        price_for_hotel = ((days - 1) * 25) * 0.65
    elif days > 15:
        price_for_hotel = ((days - 1) * 25) * 0.50
elif room_type == "president apartment":
    if days < 10:
        price_for_hotel = ((days - 1) * 35) * 0.90
    elif 10 <= days <= 15:
        price_for_hotel = ((days - 1) * 35) * 0.85
    elif days > 15:
        price_for_hotel = ((days - 1) * 35) * 0.80

if rate == "positive":
    price_for_hotel = price_for_hotel * 1.25
elif rate == "negative":
    price_for_hotel = price_for_hotel * 0.90

print(f"{price_for_hotel:.2f}")