import numpy as np
import pdb

def dangerSum(datalist):
    riskSum = 0
    
    for y in range(len(datalist)):
        for x in range(len(datalist[0])):
            if y==0: above = 10
            else: above = datalist[y-1][x]
            if y==len(datalist)-1: below = 10
            else: below = datalist[y+1][x]
            if x == 0: left = 10
            else: left = datalist[y][x-1]
            if x == len(datalist[0])-1: right = 10
            else: right = datalist[y][x+1]
            compareValues = above, below, left, right
            riskSum += determineMinimum(datalist[y][x], compareValues)
    return riskSum

def determineMinimum(spot, compareValues):
    compareValues = list(map(int, compareValues))
    spot = int(spot)
    if all((spot<value) for value in compareValues): return spot+1
    else: return 0
    
def basins(floor):
    listOfBasins=[]
    for y in range(len(floor)):
        for x in range(len(floor[0])):
            if int(floor[y][x])!=9:
                 listOfBasins = checkAdjectent(y, x, len(floor)-1, len(floor[0])-1, listOfBasins)
    #print(listOfBasins)
    sizes = []
    for basin in listOfBasins:
        sizes.append(len(basin))
    sizes.sort(reverse=True)
    print(sizes)
    return sizes[0]*sizes[1]*sizes[2]    

def checkAdjectent(y, x, maxy, maxx, basinList):
    neighbours = []
    if y > 0: neighbours.append((y-1, x))
    if y < maxy: neighbours.append((y+1, x))
    if x > 0: neighbours.append((y, x-1))
    if x < maxx: neighbours.append((y, x+1))

    appends = []
    for basin in basinList:
        if any((neighbour in basin) for neighbour in neighbours):
            appends.append(basin)
    if len(appends) == 0:
        basinList.append([(y, x)])      
    elif len(appends) >= 1:
        newBasin = []
        for bas in appends:
            basinList.remove(bas)
            for coords in bas:
                newBasin.append(coords)
        newBasin.append((y, x))
        basinList.append(newBasin)
    return basinList

#MainPart:
filename = '2021_09.txt'
data = list(np.loadtxt(filename, dtype=str))


#print(dangerSum(data))
print('product of biggest basins:', basins(data))
        
        
        
