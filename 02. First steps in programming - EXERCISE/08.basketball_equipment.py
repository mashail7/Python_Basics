annual_price = int(input())

sneakers = annual_price - (annual_price * 0.40)
suit = sneakers - (sneakers * 0.20)
ball = suit - (suit * 0.75)
accessories = ball - (ball * 0.80)

total = annual_price + sneakers + suit + ball + accessories

print(total)