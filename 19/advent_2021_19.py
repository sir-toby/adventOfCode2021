import numpy as np
import re
import pdb
 
def inputfile(fileName):
    file = open(fileName, mode='r')
    txt = file.read()
    txt = re.split('\n\n--- scanner \d+ ---\n', txt)
    breakpoint()
    txt[0] = txt[0][txt[0].index('\n')+1:]
    scannerList = []
    for scanner in txt:
        scannerCoords = []
        for coordinate in scanner.split('\n'):
            scannerCoords.append(list(map(int, coordinate.split(','))))
        scannerList.append(scannerCoords)
    return scannerList
      
def absoluteValues(scannerList):
    absScannerList = []
    for scanner in scannerList:
        absRefList = []
        for coordinate in scanner:
            absRef = 0
            for i in range(0, 3):
                absRef += coordinate[i]**2
            absRefList.append(absRef)
        reference = scanner[absRefList.index(min(absRefList))]
        print(reference)
        absScanner = []
        for coordinate in scanner:
            difference = [0, 0, 0]
            absCoord = 0
            for i in range(0, 3):
                difference[i] = coordinate[i]-reference[i]
                absCoord += difference[i]**2
            absScanner.append(absCoord)
        absScannerList.append(absScanner)
    return absScannerList

def findMatches(absList):
    for scanner in absList:
        for scanner2 in absList:
            matched = 0
            if scanner == scanner2: continue
            for abs1 in scanner:
                for abs2 in scanner2:
                    if abs1 == abs2:
                        matched += 1
            print(matched)
            
    

# Main Part

fileName = '2021_19.txt'
coordinateList = inputfile(fileName)
absList = absoluteValues(coordinateList)
findMatches(absList)
