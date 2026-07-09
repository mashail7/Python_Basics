PENS_PRICE = 5.80
MARKER_PRICE = 7.20
PREPARATION_PRICE = 1.20

pens_amount = int(input())
marker_amount = int(input())
preparation_amount = int(input())
discount_percent = int(input()) / 100

pens_total = pens_amount * PENS_PRICE
marker_total = marker_amount * MARKER_PRICE
preparation_total = preparation_amount * PREPARATION_PRICE
total_before_discount = pens_total + marker_total + preparation_total

total_after_discount = total_before_discount - (total_before_discount * discount_percent)

print(total_after_discount)