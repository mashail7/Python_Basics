from math import floor

tournaments = int(input())
starting_points = int(input())
total = starting_points
tournaments_won = 0

for i in range(1, tournaments + 1):
    round_finished = str(input())
    if round_finished == "W":
        total += 2000
        tournaments_won += 1
    elif round_finished == "F":
        total += 1200
    elif round_finished == "SF":
        total += 720

print(f"Final points: {total}")
print(f"Average points: {floor((total - starting_points) / tournaments)}")
print(f"{(tournaments_won / tournaments) * 100:.2f}%")