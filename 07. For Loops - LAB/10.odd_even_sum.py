n = int(input())
odd_sum = 0
even_sum = 0

for i in range(1, n + 1):
    new_number = int(input())
    if i % 2 == 0:
        even_sum += new_number
    else:
        odd_sum += new_number

if even_sum == odd_sum:
    print(f"Yes\nSum = {odd_sum}")
else:
    print(f"No\nDiff = {abs(even_sum - odd_sum)}")