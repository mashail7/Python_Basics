fuel_type = input()
fuel_amount = float(input())
promotion_card = input()

GASOLINE = 2.22
DIESEL = 2.33
GAS = 0.93

total = 0

if fuel_type == "Gasoline":
    if promotion_card == "Yes":
        total= fuel_amount * (GASOLINE - 0.18)
    elif promotion_card == "No":
        total = fuel_amount * GASOLINE
elif fuel_type == "Diesel":
    if promotion_card == "Yes":
        total = fuel_amount * (DIESEL - 0.12)
    elif promotion_card == "No":
        total = fuel_amount * DIESEL
elif fuel_type == "Gas":
    if promotion_card == "Yes":
        total = fuel_amount * (GAS - 0.08)
    elif promotion_card == "No":
        total = fuel_amount * GAS

if 20 <= fuel_amount <= 25:
    total = total * 0.92
elif 25 < fuel_amount:
    total = total * 0.90

print(f"{total:.2f} lv.")