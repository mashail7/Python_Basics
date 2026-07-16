cubic_meter_price = 7.61
discount_for_cubic_meter = 0.18

cubic_meters = float(input())
total_before_discount = cubic_meter_price * cubic_meters

discount = total_before_discount * discount_for_cubic_meter
final_price = (cubic_meter_price * cubic_meters) - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is {discount} lv.")