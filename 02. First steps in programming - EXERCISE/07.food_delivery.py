CHICKEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEGETARIAN_MENU_PRICE = 8.15

DESERT_PRICE = 0.20
DELIVERY_PRICE = 2.50

chicken_menu_amount = int(input())
fish_menu_amount = int(input())
vegetarian_menu_amount = int(input())

total_chicken_menu = chicken_menu_amount * CHICKEN_MENU_PRICE
total_fish_menu = fish_menu_amount * FISH_MENU_PRICE
total_vegetarian_menu = vegetarian_menu_amount * VEGETARIAN_MENU_PRICE

total_without_desert = total_chicken_menu + total_fish_menu + total_vegetarian_menu
total_with_desert = total_without_desert + (total_without_desert * DESERT_PRICE)

total = total_with_desert + DELIVERY_PRICE

print(total)