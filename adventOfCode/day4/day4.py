from utils.file_reader import read_all_file
from utils.converter import index_of
import re


lines = read_all_file('day4/day4.txt')

numbers = [int(bingo) for bingo in lines[0].split(',')]

grids = []

for i in range(2, len(lines)):
    if (i - 2) % 6 == 0:
        values = []
        for j in range(i, i+5):
            separated_values = re.findall(r'\s?(\s*\S+)', lines[j].rstrip())
            values.append([int(value.strip()) for value in separated_values])

        grids.append([values, [[0, 0, 0, 0, 0] for k in range(0, 5)], 0])


for bingo_number in numbers:
    non_finished_grids = [grid for grid in grids if grid[2] == 0]

    for grid in non_finished_grids:
        if grid[2] == 0:
            searched = grid[0]
            for i in range(0, 5):
                found_index = index_of(bingo_number, searched[i])
                if found_index != -1:
                    grid[1][i][found_index] = 1

            result = grid[1]
            somme = 0
            vert = 0
            horiz = 0

            for i in range(0, 5):
                for j in range(0, 5):
                    if result[i][j] == 1:
                        horiz = horiz + 1

                if horiz == 5:
                    grid[2] = 1
                    for j in range(0, 5):
                        for i in range(0, 5):
                            if result[i][j] == 0:
                                somme = somme + grid[0][i][j]
                    print(somme * bingo_number)

                    break
                horiz = 0

            for j in range(0, 5):
                for i in range(0, 5):
                    if result[i][j] == 1:
                        vert = vert + 1

                if vert == 5:
                    grid[2] = 1
                    for j in range(0, 5):
                        for i in range(0, 5):
                            if result[i][j] == 0:
                                somme = somme + grid[0][i][j]
                    print(somme * bingo_number)

                    break
                vert = 0