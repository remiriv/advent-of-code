fishstate = [0] * 9
days = 256

with open('day6/day6.txt') as file:
    fish = [int(x) for x in file.readline().strip().split(",")]

for f in fish:
    fishstate[f] += 1

for i in range(days):
    fishstate = fishstate[1:] + fishstate[:1]
    print(i, fishstate, sum(fishstate))
    fishstate[7] += fishstate[0]
print(fishstate, sum(fishstate))