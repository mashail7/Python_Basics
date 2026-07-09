length = int(input())
width = int(input())
height = int(input())
used_space = float(input()) / 100

fish_tank_cubic_centimeters = length * width * height
fish_tank_liters = fish_tank_cubic_centimeters * 0.001

fish_tank_without_used_space = fish_tank_liters - (fish_tank_liters * used_space)

print (fish_tank_without_used_space)