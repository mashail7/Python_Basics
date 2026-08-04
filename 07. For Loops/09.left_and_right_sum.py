n = int(input())
left_sum = 0
right_sum = 0

for i in range(1, (n * 2) + 1):
    new_number = int(input())

    if i <= (n * 2) / 2:
        left_sum += new_number
    else:
        right_sum += new_number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")