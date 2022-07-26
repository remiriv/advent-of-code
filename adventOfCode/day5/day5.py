from utils.file_reader import read_all_file
from utils.converter import index_of
import re


with open('day5/day5.txt') as file:
    coordinates = []
    result = [[0 for k in range(0, 1000)] for j in range(0,1000)]
    lines = file.readlines()
    for line in lines:
        start = line.split(' -> ')[0].split(',')
        end = line.split(' -> ')[1].split('\n')[0].split(',')
        coordinates.append([start, end])

    for coordinate in coordinates:
        if coordinate[0][0] == coordinate[1][0]:
            mini = min(int(coordinate[0][1]), int(coordinate[1][1]))
            maxi = max(int(coordinate[0][1]), int(coordinate[1][1]))
            for y in range(mini, maxi + 1):
                result[int(coordinate[0][0])][y] = result[int(coordinate[0][0])][y] + 1
        elif coordinate[0][1] == coordinate[1][1]:
            mini = min(int(coordinate[0][0]), int(coordinate[1][0]))
            maxi = max(int(coordinate[0][0]), int(coordinate[1][0]))
            for x in range(mini, maxi + 1):
                result[x][int(coordinate[1][1])] = result[x][int(coordinate[1][1])] + 1
        else:
            mini_x = min(int(coordinate[0][0]), int(coordinate[1][0]))
            maxi_x = max(int(coordinate[0][0]), int(coordinate[1][0]))
            mini_y = min(int(coordinate[0][1]), int(coordinate[1][1]))
            maxi_y = max(int(coordinate[0][1]), int(coordinate[1][1]))

            if (int(coordinate[0][0]) < int(coordinate[1][0]) and int(coordinate[0][1]) > int(coordinate[1][1])) \
                or (int(coordinate[0][0]) > int(coordinate[1][0]) and int(coordinate[0][1]) < int(coordinate[1][1]) ):
                sens = 'down'
                y = maxi_y
            else:
                sens = 'up'
                y = mini_y

            for x in range(mini_x, maxi_x + 1):
                result[x][y] = result[x][y] + 1
                if sens == 'up':
                    y = y + 1
                else:
                    y = y - 1

    count = 0
    for i in range(0,1000):
        for j in range(0,1000):
            if result[i][j] >= 2:
                count = count + 1

    print(result)
    print(count)