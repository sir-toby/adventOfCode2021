import numpy as np
import pdb

def importData(file):
    inputFile = open(file, mode = 'r')
    text = inputFile.read()
    
    coordinates = text[:text.find('\n\n')].split('\n')
    coordinateList = []
    for dot in coordinates:
        newDot = list(map(int, dot.split(',')))
        coordinateList.append(newDot)  

    folds = text[text.find('\n\n')+2:].split('\n')
    foldList = []
    for line in folds:
        fold = ['',0]
        fold[0] = line[line.find('=')-1]
        fold[1] = int(line[line.find('=')+1:])
        foldList.append(fold)
        
    sheet = createMap(foldList, coordinateList)
    return sheet, foldList

def createMap(foldList, coordinateList):
    x = 0
    y = 0
    for i in range(0, 2):
        if foldList[i][0] == 'x': x = 2*foldList[i][1]+1
        elif foldList[i][0] == 'y': y = 2*foldList[i][1]+1
    emptyMap = [[0 for w in range(x)] for h in range(y)]
    for coordinate in coordinateList:
        emptyMap[coordinate[1]][coordinate[0]] = 1
    return emptyMap

def folding(sheet, where):
    if where[0] == 'y':
        sheet = fold(sheet, where[1])
    elif where[0] == 'x':
        sheet = list(map(list, zip(*sheet)))
        sheet = fold(sheet, where[1])
        sheet = list(map(list, zip(*sheet)))
    else: print('Error')
    return sheet    
        
def fold(sheet, y):   
    for i in range(0, y):
        for j in range(len(sheet[0])):
            sheet[i][j] += sheet[len(sheet)-1-i][j]
    sheet = sheet[:y]
    return sheet

def countVisible(sheet):
    count = 0
    for line in sheet:
        for e in line:
            if e != 0: count += 1
    return(count)

def readable(sheet):
    output = ''
    for line in sheet:
        for char in line:
            if char == 0: output += ' '
            else: output += '#'
        output += '\n'
    return output    

# Main Part
filename = '2021_13.txt'
sheet, foldlist = importData(filename)
for f in foldlist:
    sheet = folding(sheet, f)

print(len(sheet), len(sheet[0]))
print(readable(sheet))

#Part 1: Only first fold:
#sheet = folding(sheet, foldlist[0])
#print(countVisible(sheet))
