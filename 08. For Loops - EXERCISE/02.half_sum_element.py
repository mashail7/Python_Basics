import sys

n = int(input())
max_num = -sys.maxsize
sum = 0

for i in range(1, n + 1):
    new_number = int(input())
    sum += new_number
    if new_number > max_num:
        max_num = new_number

if sum - max_num == max_num:
    print("Yes")
    print(f"Sum = {sum - max_num}")
else:
    print("No")
    print(f"Diff = {abs(max_num - (sum - max_num))}")