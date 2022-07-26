from utils.converter import binary_to_int

''' PART 1
with open('day3/day3.txt') as file:
    lines = file.readlines()

    result = [[0,0] for i in range(0, 12)]

    for line in lines:
        result = [[result[i][0] + 1, result[i][1]] if line[i] == '0' else [result[i][0], result[i][1] + 1] for i in range(0,12)]

    alpha_ray_bin = ''.join(['0' if result[i][0] > result[i][1] else '1' for i in range(0,12)])
    alpha = binary_to_int(alpha_ray_bin)

    gamma_ray_bin = ''.join(['1' if result[i][0] > result[i][1] else '0' for i in range(0,12)])
    gamma = binary_to_int(gamma_ray_bin)

    print(alpha*gamma)
    
'''

def get_predominant_and_lines(lines, position):
    bit = [0, 0]
    zero_lines = []
    one_lines = []

    for line in lines:

        if line[position] == '0':
            bit[0] = bit[0] + 1
            zero_lines.append(line)
        else:
            bit[1] = bit[1] + 1
            one_lines.append(line)

    predominant = 1 if bit[1] > bit[0] else (0 if bit[0] > bit[1] else 2)
    return predominant, zero_lines, one_lines


with open('day3/day3.txt') as file:
    lines = file.readlines()

    predominant, zero_lines, one_lines = get_predominant_and_lines(lines, 0)

    oxygen_lines = one_lines if predominant == 1 else zero_lines
    co2_lines = zero_lines if predominant == 1 or predominant == 2 else one_lines

    for position in range(1, 12):
        if len(oxygen_lines) > 1:
            predominant, zero_lines, one_lines = get_predominant_and_lines(oxygen_lines, position)
            oxygen_lines = one_lines if (predominant == 1 or predominant == 2) and len(one_lines) > 0 else zero_lines

        if len(co2_lines) > 1:
            predominant, zero_lines, one_lines = get_predominant_and_lines(co2_lines, position)
            co2_lines = zero_lines if (predominant == 1 or predominant == 2) and len(zero_lines) > 0 else one_lines

    oxygen = binary_to_int(oxygen_lines[0][0:12])
    co2 = binary_to_int(co2_lines[0][0:12])

    print (oxygen*co2)