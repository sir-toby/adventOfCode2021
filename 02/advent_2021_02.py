import numpy as np

filename = 'C:\\Users\\tbachmann\\Desktop\\Advent of coding\\2021_2.txt'

data = np.loadtxt(filename, dtype=str)
datalist = data.tolist()
horizontal = 0
vertical = 0

for i in datalist:

    match i[0]:
        case 'forward':
            horizontal += + int(i[1])
        case 'up':
            vertical -= int(i[1])
        case 'down':
            vertical += int(i[1])

print(horizontal*vertical)

    

