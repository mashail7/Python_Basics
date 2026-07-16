deposit = float(input())
deposit_term = int(input())
interest_rate = float(input()) / 100

total = deposit + deposit_term * ((deposit * interest_rate) / 12)

print(total)