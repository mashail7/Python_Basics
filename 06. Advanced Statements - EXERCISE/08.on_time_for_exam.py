exam_hour = int(input())
exam_minute = int(input())
hour_of_coming = int(input())
minute_of_coming = int(input())

exam_in_minutes = exam_hour * 60 + exam_minute
coming_in_minutes = hour_of_coming * 60 + minute_of_coming
difference = 0

if exam_in_minutes >= coming_in_minutes:
    difference = exam_in_minutes - coming_in_minutes
    if difference > 30:
        print("Early")
        hours_earlier = difference // 60
        minutes_earlier = difference % 60
        if hours_earlier >= 1:
            print(f"{hours_earlier}:{minutes_earlier:02d} hours before the start")
        elif hours_earlier < 1:
            print(f"{minutes_earlier} minutes before the start")
    elif 0 <= difference <= 30:
        print("On time")
        if difference != 0:
            print(f"{difference} minutes before the start")
elif exam_in_minutes < coming_in_minutes:
    difference = coming_in_minutes - exam_in_minutes
    hours_late = difference // 60
    minutes_late = difference % 60
    print("Late")
    if hours_late >= 1:
        print(f"{hours_late}:{minutes_late:02d} hours after the start")
    elif hours_late < 1:
        print(f"{minutes_late} minutes after the start")