import numpy as np
import pdb
import copy

def importFile(fileName):
    seaFloor = ((open(fileName, 'r')).read()).split('\n')
    newFile = []
    for line in seaFloor:
        newFile.append(list(line))        
    return newFile
    
def step(floor):
    floor = horizontal(floor)
    floor = vertical(floor)
    return floor

def horizontal(floorHor):
    newFloor = copy.deepcopy(floorHor)
    for y in range(len(floorHor)):
        for x in range(len(floorHor[y])-1):
            if floorHor[y][x] == '>' and floorHor[y][x+1] == '.':
                newFloor[y][x+1] = '>'
                newFloor[y][x] = '.'
        if floorHor[y][len(floorHor[y])-1] == '>' and floorHor[y][0] == '.':
            newFloor[y][0] = '>'
            newFloor[y][len(floorHor[y])-1] = '.'
    return newFloor
        
def vertical(floorVer):
    newFloor2 = copy.deepcopy(floorVer)
    for x in range(len(floorVer[0])):
        for y in range(len(floorVer)-1):
            if floorVer[y][x] == 'v' and floorVer[y+1][x] == '.':
                newFloor2[y+1][x] = 'v'
                newFloor2[y][x] = '.'
        if floorVer[len(floorVer)-1][x] == 'v' and floorVer[0][x] == '.':
            newFloor2[0][x] = 'v'
            newFloor2[len(floorVer)-1][x] = '.'
    return newFloor2

def readable(uglyFloor):
    niceFloor = ''
    for line in uglyFloor:
        niceFloor += ''.join(line) + '\n'
    return niceFloor

# Main Part

fileName = '2021_25.txt'
seaFloor = importFile(fileName)

count = 0
while True:
    count += 1
    seaFloorNew = step(seaFloor)
    if seaFloorNew == seaFloor: break
    seaFloor = seaFloorNew

print(readable(seaFloor))
print(count)
