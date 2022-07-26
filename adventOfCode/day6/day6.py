import math

from utils.file_reader import read_all_file
from utils.converter import index_of
import re

'''
with open('day6/day6.txt') as file:
    lantern = list(map(lambda ttl: int(ttl), file.readlines()[0].split(',')))

    number_of_fish = {}
    for days in range(0, 256):
        new_fish = sum(1 for value in lantern if value == 0)
        lantern = list(map(lambda ttl: ttl - 1 if ttl > 0 else 6, lantern))
        number_of_fish[days] = (number_of_fish.get(days-1, 0) if days > 0 else len(lantern)) + new_fish
        print("test", number_of_fish.get(days+9))
        number_of_fish[days+9] = number_of_fish.get(days+9, 0) + new_fish
        for i in range(0, math.ceil((256-days)/6)):
            print(new_fish)
            number_of_fish[days + 9 + 7*i] = number_of_fish.get(days + 9 + 7*i, 0) + new_fish
        print(days)
        print(number_of_fish[days])
        print('------')
'''


with open('day6/day6.txt') as file:
    lantern = list(map(lambda ttl: int(ttl), file.readlines()[0].split(',')))

    number_of_fish = {}
    for days in range(0, 256):
        new_fish = sum(1 for value in lantern if value == 0)

        lantern = list(map(lambda ttl: ttl - 1 if ttl > 0 else 6, lantern))

        number_of_fish[days] = number_of_fish.get(days, 0) + (number_of_fish.get(days-1, 0) if days > 0 else len(lantern)) + new_fish
        number_of_fish[days+9] = number_of_fish.get(days+9, 0) + new_fish

        if new_fish > 0:
            for i in range(1, math.ceil((256-days)/6) + 2):
                print(new_fish)
                print(i)
                number_of_fish[days + 9 + 7*i] = number_of_fish.get(days + 9 + 7*i, 0) + new_fish
        print(days)
        print(number_of_fish[days])
        print('------')
