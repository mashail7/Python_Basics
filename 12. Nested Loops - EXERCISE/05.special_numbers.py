n = int(input())


for number in range(1111, 9999 + 1):
    number_to_str = str(number)
    for digit in number_to_str:

        flag = False

        if digit == "0":
            flag = False
            break

        if n % int(digit) == 0:
            flag = True
        else:
            flag = False
            break
    if flag:
        print(number, end=" ")