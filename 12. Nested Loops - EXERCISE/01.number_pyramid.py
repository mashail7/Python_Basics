n = int(input())
count = 1
is_bigger_than_n = False

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if count > n:
            is_bigger_than_n = True
            break
        print(str(count) + " ", end= "")
        count += 1
    if is_bigger_than_n == True:
        break
    print() 