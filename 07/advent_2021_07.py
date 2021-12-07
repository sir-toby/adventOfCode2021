import numpy as np
import statistics as stat


def  part1(positions):
    fuel = 0
    median = stat.median(positions)
    for boat in positions:
        fuel += abs(boat-median)
    return int(fuel), int(median)

def part2(positions):
    fuellist = []
    for pos in range(0, max(positions)):
        fuel = 0
        for boat in positions:
            difference = abs(boat-pos)
            fuel += (1+(difference-1)/2)*difference
        fuellist.append(fuel)
    return int(min(fuellist)), int(fuellist.index(min(fuellist)))
        

#MainPart:

filename = '2021_07.txt'

datalist = list(map(int, np.loadtxt(filename, dtype=str, delimiter=',').tolist()))

amount, position = part1(datalist)
amount2, position2 = part2(datalist)

print('Part 1: The boats require ', amount, ' fuel to reach position ', position)
print('Part 2: The boats require ', amount2, ' fuel to reach position ', position2)
