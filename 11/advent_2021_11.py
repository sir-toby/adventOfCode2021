import numpy as np
import pdb

def extendMatrix(matrix, value):
    newMatrix = []
    height = len(matrix)
    width = len(matrix[0])+2
    newMatrix.append([value]*width)
    for line in matrix:
        newline = [value]
        for char in line:
            newline.append(int(char))
        newline.append(value)
        newMatrix.append(newline)
    newMatrix.append([value]*width)
    return newMatrix

def removeBorder(borderMatrix):
    borderlessMatrix = []
    for row in borderMatrix:
        borderlessMatrix.append(row[1:-1])
    borderlessMatrix = borderlessMatrix[1:-1]
    return borderlessMatrix

def niceResult(matrixUgly):
    nice = ''
    for row in matrixUgly:
        niceLine = ''.join(map(str, row)) + '\n'
        nice += (niceLine)
    return nice

def emptyMatrix(mix):
    empty = []
    for i in range(len(mix)):
        empty.append([])
        for j in range(len(mix[0])):
            empty[i].append(False)
    return empty

def part1(theMatrix, steps):
    flashNumber = 0
        
    for i in range(steps):
        flashMatrix = emptyMatrix(theMatrix)
        #Step 1: increase energy level
        for height in range(len(theMatrix)):
            for width in range(len(theMatrix[0])):
                theMatrix[height][width] += 1
        #Step 2: check for flashes
        for height in range(len(theMatrix)):
            for width in range(len(theMatrix[0])):
                if theMatrix[height][width] >9:
                    theMatrix = flash(theMatrix, flashMatrix, height, width)
        #Step 3: Set flashed octopusses to 0
        for height in range(len(theMatrix)):
            for width in range(len(theMatrix[0])):
                if theMatrix[height][width] > 9:
                    flashNumber = flashNumber+1
                    theMatrix[height][width] = 0
    return theMatrix, flashNumber

def oneStep(theMatrix, flashMatrix):
    #Step 1: increase energy level
    for height in range(len(theMatrix)):
        for width in range(len(theMatrix[0])):
            theMatrix[height][width] += 1
    #Step 2: check for flashes
    for height in range(len(theMatrix)):
        for width in range(len(theMatrix[0])):
            if theMatrix[height][width] >9:
                theMatrix = flash(theMatrix, flashMatrix, height, width)
    #Step 3: Set flashed octopusses to 0
    flashes = 0
    for height in range(len(theMatrix)):
        for width in range(len(theMatrix[0])):
            if theMatrix[height][width] > 9:
                flashes +=1
                theMatrix[height][width] = 0
    return theMatrix, flashes

def flash(matrixFlash, flashMap, y, x):
    if flashMap[y][x] == True: return matrixFlash
    else: flashMap[y][x] = True
    for ver in range(y-1, y+2):
        for hor in range(x-1, x+2):
            matrixFlash[ver][hor] += 1
            if matrixFlash[ver][hor] >9:
                matrixFlash = flash(matrixFlash, flashMap, ver, hor)
    
    return matrixFlash
                
def part1(inputMap, steps):
    flashNumber = 0
    for i in range(steps):
        emptyMat = emptyMatrix(inputMap)
        inputMap, flashNumberStep = oneStep(inputMap, emptyMat)
        flashNumber += flashNumberStep
    return inputMap, flashNumber
        
def part2(inputMap):
    currentStep = 0
    synchronized = False
    while synchronized == False:
        currentStep += 1
        emptyMat = emptyMatrix(inputMap)
        inputMap, ignore = oneStep(inputMap, emptyMat)
        borderless = removeBorder(inputMap)
        for row in borderless:
            synchronized = True
            if row != borderless[0]:
                synchronized = False
                break
    return currentStep
        

#MainPart:
filename = '2021_11.txt'
step = 435


data = list(np.loadtxt(filename, dtype=str))
newData = []
for line in data:
    newData.append(list(line))

extendedMatrix = extendMatrix(newData, -999999)
#resultMatrix, flashes = part1(extendedMatrix, step)

#print(niceResult(removeBorder(resultMatrix)), flashes)
print(part2(extendedMatrix))

