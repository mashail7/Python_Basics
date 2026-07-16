VIDEO_CARD = 250

budget = float(input())
video_cards = int(input())
processors = int(input())
ram_storage = int(input())

video_card_total = video_cards * VIDEO_CARD
total_price = video_card_total + ((video_card_total * 0.10) * ram_storage) + ((video_card_total * 0.35) * processors)

if video_cards > processors:
    total_price = total_price * 0.85

if total_price <= budget:
    money_left = budget - total_price
    print(f"You have {money_left:.02f} leva left!")
elif total_price > budget:
    money_needed = total_price - budget
    print(f"Not enough money! You need {money_needed:.02f} leva more!")