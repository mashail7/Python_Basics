km = int(input())
tariff = input("")

price = 0

if km < 20:
    START = 0.70
    DAY_TARIFF = 0.79
    NIGHT_TARIFF = 0.90
    if tariff == "day":
        price = START + (km * DAY_TARIFF)
    elif tariff == "night":
        price = START + (km * NIGHT_TARIFF)
elif 20 <= km < 100:
    TARIFF = 0.09
    price = km * TARIFF
elif 100 <= km:
    TARIFF = 0.06
    price = km * TARIFF

print(f"{price:.02f}")