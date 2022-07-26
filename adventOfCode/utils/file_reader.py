import os
dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def read_all_file(filename):
    with open(f"{dir_path}/{filename}") as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]

'''
def read_line_by_line(filename):
    with open(filename) as file:
        for line in file:
            print(line.rstrip())
'''

