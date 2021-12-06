import numpy as np
import pdb


def importToList(text):
    listOfCoordinates = []
    data = np.loadtxt(filename, dtype=str, delimiter=' -> ')
    inputs = data.tolist()
    print(inputs)
    for item in inputs:
        line = []
        for coordinate in item:
            line.append(list(map(int, list(coordinate.split(",")))))
        listOfCoordinates.append(line)
    return listOfCoordinates    

def size(ventList):
    x = 0
    y = 0
    for vents in ventList:
        for coordinate in vents:
            if int(coordinate[0])>x: x = int(coordinate[0])
            if int(coordinate[1])>y: y = int(coordinate[1])
    floor = [[0 for w in range(x+1)] for h in range(y+1)]
    print(len(floor[0]), len(floor))
    return floor
            
def onlyHorizontalVertical(ventList):
    newVentList = []
    for vents in ventList:
        ventsTransposed = transpose(vents)
        if vents[0][0] == vents[1][0]:
            newVentList.append(vents)
        if vents[0][1] == vents[1][1]:
            newVentList.append(vents)
    print(newVentList)
    return newVentList

def drawLines(ventList, floor):
    for vents in ventList:
        if vents[0][0] == vents[1][0]:            
            x = vents[0][0]
            low, high, step = steps(vents[0][1], vents[1][1])
            for y in range(low, high+step, step):
                floormap[y][x] += 1
        elif vents[0][1] == vents[1][1]:
            y = vents[0][1]
            low, high, step = steps(vents[0][0], vents[1][0])
            for x in range(low, high+step, step):
                floor[y][x] += 1
        else:
            low, high, step = steps(vents[0][1], vents[1][1])
            low2, high2, step2 = steps(vents[0][0], vents[1][0])

            x = low2
            for y in range(low, high+step, step):
                floor[y][x] += 1
                x += step2
            
    return floor

def determineBorders(a, b):
    if a < b:
        low = a
        high = b+1
    else:
        low = b
        high = a+1
    return low, high

def steps(a, b):
    if a<b:
        step = 1
    elif a>b:
        step = -1
    else:
        step = 0
    
    return a, b, step

def countDanger(floor):
    count = 0
    for row in floor:
        for c in row:
            if c > 1:
                count += 1
    return count
    

filename = 'C:\\Users\\tbachmann\\Desktop\\Advent of coding\\2021_5.txt'

listOfMatrices = importToList(filename)
floormap = size(listOfMatrices)
lines = drawLines(listOfMatrices, floormap)
dangerCount = countDanger(floormap)
print(dangerCount)
linesreadable = ''
for rows in lines:
    for chars in rows:
        linesreadable += str(chars)
    linesreadable += '\n'
print(linesreadable)
