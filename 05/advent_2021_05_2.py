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
    return floor
            
def onlyHorizontalVertical(ventList):
    newVentList = []
    for vents in ventList:
        if vents[0][0] == vents[1][0]:
            newVentList.append(vents)
        if vents[0][1] == vents[1][1]:
            newVentList.append(vents)
    return newVentList

def drawLines(ventDescription, floor):
    for vents in ventDescription:
        low, high, step = steps(vents[0][1], vents[1][1])
        low2, high2, step2 = steps(vents[0][0], vents[1][0])
        if step2 == 0:
            x = low2
            for y in range(low, high+step, step):
                floor[y][x] += 1
                x += step2
        else: 
            y = low
            for x in range(low2, high2+step2, step2):
                floor[y][x] += 1
                y += step
    ventDescription = None
    return floor

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

def linesreadable(floormap):
    output = ''
    for rows in floormap:
        for chars in rows:
            output += str(chars)
        output += '\n'
    return output

def part1(ventList):
    emptyMap1 = size(listOfMatrices)
    ventList = onlyHorizontalVertical(ventList)
    filledMap1 = drawLines(ventList, emptyMap1)
    dangercount = countDanger(filledMap1)
    print('Non-diagonal lines:\nFound dangerzones:', dangercount)
    print(linesreadable(filledMap1))

def part2(ventList2):
    emptyMap2 = size(listOfMatrices)
    filledMap2 = drawLines(ventList2, emptyMap2)
    dangercount = countDanger(filledMap2)
    print('All lines:\nFound dangerzones:', dangercount)
    print(linesreadable(filledMap2))

filename = 'C:\\Users\\tbachmann\\Desktop\\Advent of coding\\2021_5.txt'

listOfMatrices = importToList(filename)

part1(listOfMatrices)
part2(listOfMatrices)

