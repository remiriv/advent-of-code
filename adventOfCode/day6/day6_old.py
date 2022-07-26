import math

from utils.file_reader import read_all_file
from utils.converter import index_of
import re

'''
with open('day6/day6.txt') as file:
    lantern = list(map(lambda ttl: int(ttl), file.readlines()[0].split(',')))

    for days in range(0, 256):
        new_fish = sum(1 for value in lantern if value == 0)
        lantern = list(map(lambda ttl: ttl - 1 if ttl > 0 else 6, lantern))
        lantern.extend([8] * new_fish)
        print(days)
        print(len(lantern))
        print('------')
'''

import sys
print("Python Recursive Limitation = ", sys.getrecursionlimit())

def new_fish_for_one(days):
    fish_ttl = [8]
    for number in range(0, days):
        new = sum(1 for value in fish_ttl if value == 0)
        fish_ttl = list(map(lambda ttl: ttl - 1 if ttl > 0 else 6, fish_ttl))
        fish_ttl.extend([8] * new)
    return fish_ttl


for days in range(0, 256):
    print('------')
    print(days)
    print(len(new_fish_for_one(days)))

'''


def get_number_of_fish(new_fish, days, number):
    fishes = [8] * new_fish
    for remaining in range(0, 256-days):
        fishes = list(map(lambda ttl: ttl - 1 if ttl > 0 else 6, fishes))
        newly_created_fish = sum(1 for value in fishes if value == 0)
        new = get_number_of_fish(newly_created_fish, remaining, number)
        number = number + newly_created_fish + new
    return number


with open('day6/day6.txt') as file:
    lantern = list(map(lambda ttl: int(ttl), file.readlines()[0].split(',')))

    number_of_fish = len(lantern)
    number = 0
    for days in range(0, 256):
        new_fish = sum(1 for value in lantern if value == 0)
        newly_created_fish = 0
        number = get_number_of_fish(new_fish, days, number)

        print(days)
        print(number_of_fish)
'''