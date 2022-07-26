def binary_to_int(binary_number):
    return int(binary_number, 2)


def index_of(val, in_list):
    try:
        return in_list.index(val)
    except ValueError:
        return -1