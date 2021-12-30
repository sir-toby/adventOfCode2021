import numpy as np
import pdb

def readPackage(binString, overallVersion):
    version = binString[:3]
    overallVersion += int(version, base=2)
    typeId = binString[3:6]
    content = binString[6:]
    #if Value-Package:
    if int(typeId, base=2) == 4:
        value = ''
        for i in range(0, len(content), 5):
            value += content[i+1:i+5]
            if content[i] == '0':
                reducedStringStart = 6 + i+5
                resultValue = int(value, base=2)
                break
    else:
    #if Operator-Package:
        value = []
        if content[0] == '0':
            subPackageLength = int(content[1:16], base=2)
            subPackages = content[16:16+subPackageLength]
            while subPackages != '':
                valueChange, overallVersion, subPackages = readPackage(subPackages, overallVersion)
                value.append(valueChange)
            reducedStringStart = 6+1+15+subPackageLength
        elif content[0] == '1':
            subPackageNumber = int(content[1:12], base=2)
            subPackages = content[12:]
            difference = 0
            for i in range(subPackageNumber):
                valueChange, overallVersion, newSubPackages = readPackage(subPackages, overallVersion)
                difference += len(subPackages)-len(newSubPackages)
                subPackages = newSubPackages
                value.append(valueChange)
            reducedStringStart = 6+1+11+difference
        else: print('Error')
        match int(typeId, base=2):
            case 0: resultValue = sum(value)
            case 1:
                resultValue = 1
                for i in value:
                    resultValue *= i
            case 2: resultValue = min(value)
            case 3: resultValue = max(value)
            case 5:
                if value[0] > value[1]: resultValue = 1
                else: resultValue = 0
            case 6:
                if value[0] < value[1]: resultValue = 1
                else: resultValue = 0
            case 7:
                if value[0] == value[1]: resultValue = 1
                else: resultValue = 0
    reducedString = binString[reducedStringStart:]
    return resultValue, overallVersion, reducedString           
            

# Main Part
filename = '2021_16.txt'
inputText = (open(filename, mode='r')).read()
inputBinary = (bin(int(inputText, base=16))[2:]).zfill(len(inputText)*4)


overallVersion = 0
value, overallVersion, newBinString = readPackage(inputBinary, overallVersion)
print(overallVersion, value)
