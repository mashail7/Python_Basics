n = int(input())
sells_made = 0
rating_total = 0
percent_sales_done = 0

for i in range(n):
    computer = int(input())

    rating = computer % 10
    rating_total += rating

    if rating == 2:
        percent_sales_done = 0
    elif rating == 3:
        percent_sales_done = 0.50
    elif rating == 4:
        percent_sales_done = 0.70
    elif rating == 5:
        percent_sales_done = 0.85
    elif rating == 6:
        percent_sales_done = 1.0

    potential_sells = computer // 10
    sells_made += potential_sells * percent_sales_done

average_rating = rating_total / n
print(f"{sells_made:.2f}")
print(f"{average_rating:.2f}")