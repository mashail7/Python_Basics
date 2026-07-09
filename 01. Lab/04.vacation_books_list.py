page_amount = int(input())
pages_per_hour = int(input())
days_amount = int(input())

needed_hours_a_day = (page_amount // pages_per_hour) / days_amount

print(needed_hours_a_day)