with open('day2/day2.txt') as file:
    lines = file.readlines()

    depth = 0
    length = 0
    aim = 0
    for line in lines:
        formatted = line.split(' ')
        value = int(formatted[1][0])
        if formatted[0] == 'forward':
            length = length + value
            depth = depth + value * aim
        if formatted[0] == 'up':
            aim = aim - value
        if formatted[0] == 'down':
            aim = aim + value

    print(length*depth)
