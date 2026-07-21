import math

MAGNOLII = 3.25
ZUMBULI = 4
ROZI = 3.50
KAKTUS = 8
TAX = 0.05

magnolii_amount = int(input())
zumbuli_amount = int(input())
rozi_amount = int(input())
kaktus_amount = int(input())
gift_price = float(input())

magnolii_total = magnolii_amount * MAGNOLII
zumbuli_total = zumbuli_amount * ZUMBULI
rozi_total = rozi_amount * ROZI
kaktus_total = kaktus_amount * KAKTUS

total_before_tax = (magnolii_total + zumbuli_total + rozi_total + kaktus_total)
total = total_before_tax - (total_before_tax * TAX)

if total >= gift_price:
    total -= gift_price
    print(f"She is left with {math.floor(total)} leva.")
elif total < gift_price:
    gift_price -= total
    print(f"She will have to borrow {math.ceil(gift_price)} leva.")