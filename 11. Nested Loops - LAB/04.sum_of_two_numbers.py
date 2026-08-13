start_number = int(input())
end_number = int(input())
magic_number = int(input())
count = 0
flag = False

for i in range(start_number,end_number + 1):
    for j in range(start_number,end_number + 1):
        count += 1
        if i + j == magic_number:
            print(f"Combination N:{count} ({i} + {j} = {magic_number})")
            flag = True
            break
        elif i == end_number and j == end_number:
            print(f"{count} combinations - neither equals {magic_number}")
    if flag == True:
        break