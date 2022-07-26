from utils import read_all_file

lines = read_all_file('day1/day1.txt')
result = 0
new_lines = []
for i in range(0, len(lines)-2):
    new_lines.append(int(lines[i]) + int(lines[i+1]) + int(lines[i+2]))
for i in range(0, len(new_lines)):
    if int(new_lines[i]) > int(new_lines[i-1]):
        result = result + 1

print(result)
