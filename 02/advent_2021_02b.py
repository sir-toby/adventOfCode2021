import numpy as np

filename = 'C:\\Users\\tbachmann\\Desktop\\Advent of coding\\2021_2.txt'

data = np.loadtxt(filename, dtype=str)

horizontal = 0
vertical = 0
aim=0

for i in data:

    match i[0]:
        case 'forward':
            horizontal += int(i[1])
            vertical += aim*int(i[1])
        case 'up':
            aim -= int(i[1])
        case 'down':
            aim += int(i[1])

print(horizontal*vertical)

    

