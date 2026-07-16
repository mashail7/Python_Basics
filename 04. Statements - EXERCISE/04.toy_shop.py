PUZZLE = 2.60
TALKING_DOLL = 3
PLUSH_BEAR = 4.10
MINION = 8.20
TRUCK = 2

vacation_price = float(input())
puzzle_quantity = int(input())
talking_doll_quantity = int(input())
plush_bear_quantity = int(input())
minion_quantity = int(input())
truck_quantity = int(input())

total_quantity_for_toys = puzzle_quantity + talking_doll_quantity + plush_bear_quantity + minion_quantity + truck_quantity

total_price_for_toys = ((puzzle_quantity * PUZZLE) + (talking_doll_quantity * TALKING_DOLL)
                        + (plush_bear_quantity * PLUSH_BEAR) + (minion_quantity * MINION)
                        + (truck_quantity * TRUCK))

if total_quantity_for_toys >= 50:
    total_price_for_toys = total_price_for_toys * 0.75

total_price_for_toys = total_price_for_toys * 0.90

if total_price_for_toys >= vacation_price:
    money_left = total_price_for_toys - vacation_price
    print(f"Yes! {money_left:.02f} lv left.")
else:
    money_left = vacation_price - total_price_for_toys
    print(f"Not enough money! {money_left:.02f} lv needed.")