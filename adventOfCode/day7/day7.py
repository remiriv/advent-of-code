with open('day7/day7.txt') as file:
    crab = [int(x) for x in file.readline().strip().split(",")]

min_fuel = 0
min_index = 0
print(min(crab))
print(max(crab)+1)
for i in range(min(crab), max(crab)+1):
    total_fuel = 0
    for position in crab:
        total_fuel += sum(value for value in range(1, abs(i - position)+1))
    if min_fuel == 0 or total_fuel < min_fuel:
        min_fuel = total_fuel
        min_index = i
    print(i)
    print(min_fuel)
    print(min_index)