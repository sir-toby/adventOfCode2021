import numpy as np
import pdb

def importFile(fileName):
    coordinateList = []
    file = open(fileName, 'r')
    text = file.read()
    text = text.split('\n')
    for line in text:
        newLine = line.split(' ')
        coordinates = newLine[1].split(',')
        xCoord = [coordinates[0][coordinates[0].find('=')+1:coordinates[0].find('..')], coordinates[0][coordinates[0].find('..')+2:]]
        yCoord = [coordinates[1][coordinates[1].find('=')+1:coordinates[1].find('..')], coordinates[1][coordinates[1].find('..')+2:]]
        zCoord = [coordinates[2][coordinates[2].find('=')+1:coordinates[2].find('..')], coordinates[2][coordinates[2].find('..')+2:]]
        newLine = [newLine[0], xCoord, yCoord, zCoord]
        coordinateList.append(newLine)
    return coordinateList
            
def initialize(instructions):
    reactorCore = [[[[0] for x in range(101)] for y in range(101)] for z in range(101)]
    for instruction in instructions:
        if (abs(int(instruction[3][0])>50) or abs(int(instruction[3][1]))>50 or
            abs(int(instruction[2][0])>50) or abs(int(instruction[2][1]))>50 or
            abs(int(instruction[1][0])>50) or abs(int(instruction[1][1]))>50):
            continue
        for z in range(int(instruction[3][0]), int(instruction[3][1])+1):
            for y in range(int(instruction[2][0]), int(instruction[2][1])+1):
                for x in range(int(instruction[1][0]), int(instruction[1][1])+1):
                    if instruction[0] == 'off': reactorCore[z][y][x] = 0
                    elif instruction[0] == 'on': reactorCore[z][y][x] = 1
        #print(countOn(reactorCore))
    return reactorCore

def countOn(reactor):
    count = 0
    for z in reactor:
        for y in z:
            for x in y:
                if x == 1: count += 1
    return count

def getReactor(instructions):
    xValues = []
    yValues = []
    zValues = []
    for instruction in instructions:
        xValues.append(instruction[1])
        yValues.append(instruction[2])
        zValues.append(instruction[3])
    xMin = int(min(list(zip(*xValues))[0]))
    xMax = int(max(list(zip(*xValues))[1]))
    yMin = int(min(list(zip(*yValues))[0]))
    yMax = int(max(list(zip(*yValues))[1]))
    zMin = int(min(list(zip(*zValues))[0]))
    zMax = int(max(list(zip(*zValues))[1]))
    reactor = [[[[0] for x in range(xMin, xMax+1)] for y in range(yMin, yMax+1)] for z in range(zMin, zMax+1)]
    return reactor

def reboot(reactor, instructions):
    for instruction in instructions:
        for z in range(int(instruction[3][0]), int(instruction[3][1])+1):
            for y in range(int(instruction[2][0]), int(instruction[2][1])+1):
                for x in range(int(instruction[1][0]), int(instruction[1][1])+1):
                    if instruction[0] == 'off': reactor[z][y][x] = 0
                    elif instruction[0] == 'on': reactor[z][y][x] = 1
    return reactor    
    

# Main Part

fileName = '2021_22.txt'
coordinateList = importFile(fileName)

#Part1
reactorCoreState = initialize(coordinateList)
print(countOn(reactorCoreState))

#Part 2
reactor = getReactor(coordinateList)
reboot(reactor, coordinateList)
print(countOn(reactorCoreState))


