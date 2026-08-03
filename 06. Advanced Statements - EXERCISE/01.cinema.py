projection = str(input())
row = int(input())
column = int(input())

if projection == "Premiere":
    total = (row * column) * 12
    print(f"{total:.02f} leva")
elif projection == "Normal":
    total = (row * column) * 7.50
    print(f"{total:.02f} leva")
elif projection == "Discount":
    total = (row * column) * 5
    print(f"{total:.02f} leva")