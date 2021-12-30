import numpy as np
import pdb

global depth
depth = 0

def readPackage(binString, overallVersion):
    global depth
    depth += 1
    breakpoint()
    version = binString[:3]
    overallVersion += int(version, base=2)
    print('Version: ', int(version, base=2), 'Overall Version:', overallVersion, depth)
    typeId = binString[3:6]
    content = binString[6:]
    #for part1:
    if int(typeId, base=2) == 4:
        value = ''
        for i in range(0, len(content), 5):
            value += content[i+1:i+5]
            if content[i] == '0':
                reducedStringStart = 6 + i+5
                value = int(value, base=2)
                break
    else:
        value = 0
        if content[0] == '0':
            try: 
                subPackageLength = int(content[1:16], base=2)
                subPackages = content[16:16+subPackageLength]
                while subPackages != '':
                    valueChange, overallVersion, subPackages = readPackage(subPackages, overallVersion)
                    value += valueChange
                reducedStringStart = 6+1+15+subPackageLength
            except: breakpoint()
        elif content[0] == '1':
            subPackageNumber = int(content[1:12], base=2)
            subPackages = content[12:]
            difference = 0
            for i in range(subPackageNumber):
                valueChange, overallVersion, newSubPackages = readPackage(subPackages, overallVersion)
                difference += len(subPackages)-len(newSubPackages)
                subPackages = newSubPackages
                value += valueChange
            reducedStringStart = 6+1+11+difference
        else: print('Error')
    reducedString = binString[reducedStringStart:]
    #print(value)
    depth -= 1
    return value, overallVersion, reducedString           
            

# Main Part
filename = '2021_16.txt'
inputFile = open(filename, mode='r')
inputText = inputFile.read()

inputBinary = (bin(int(inputText, base=16))[2:]).zfill(len(inputText)*4)

overallVersion = 0
count = 0

while inputBinary != '':
    count += 1
    print('Count:', count)
    if int(inputBinary, base=2) == 0: break
    value, overallVersion, newBinString = readPackage(inputBinary, overallVersion)
    if (len(inputBinary)-len(newBinString))%4 == 0:
        inputBinary = newBinString
    else:
        difference = len(inputBinary)-len(newBinString)+4-(len(inputBinary)-len(newBinString))%4
        inputBinary = inputBinary[difference:]
print(overallVersion)


#AAAAAAAAAAA
#BBBBB BBBBB
#cc cc CC CC

