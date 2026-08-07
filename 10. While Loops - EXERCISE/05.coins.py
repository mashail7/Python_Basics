change = float(input())
change_in_coins = int(change * 100)
coins = 0

while change_in_coins > 0:
    coins += change_in_coins // 200
    change_in_coins = change_in_coins % 200
    coins += change_in_coins // 100
    change_in_coins = change_in_coins % 100
    coins += change_in_coins // 50
    change_in_coins = change_in_coins % 50
    coins += change_in_coins // 20
    change_in_coins = change_in_coins % 20
    coins += change_in_coins // 10
    change_in_coins = change_in_coins % 10
    coins += change_in_coins // 5
    change_in_coins = change_in_coins % 5
    coins += change_in_coins // 2
    change_in_coins = change_in_coins % 2
    coins += change_in_coins // 1
    change_in_coins = change_in_coins % 1

print(coins)