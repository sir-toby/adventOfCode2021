import numpy as np

def dataimport(data):
    output=[]
    for entry in data:
        line=[]
        line.append(sortList(entry[0].split()))
        line.append(sortList(entry[1].split()))
        output.append(line)
    return output
        
def part1(inputData):
    count = 0
    for output in inputData:
        for number in output[1]:
            if len(number) == 2 or len(number) == 3 or len(number)== 4 or len(number)== 7:
                count +=1
    return count
            
def part2(inputData):
    endSum = 0
    for entries in inputData:
        mapping = determineNumbers(entries[0])
        endSum += getNumber(mapping, entries[1])
    return endSum
        
def determineNumbers(numbersCombined):
    sortedNumbers=['']*10
    numbersCombined.sort(key=len)
    for number in numbersCombined:
        match len(number):
            case 2:
                sortedNumbers[1]=number
            case 3:
                sortedNumbers[7]=number
            case 4:
                sortedNumbers[4]=number
            case 5:
                if all((letter in number) for letter in sortedNumbers[7]):
                    sortedNumbers[3] = number
                else:
                    match = 0
                    for letter in sortedNumbers[4]:
                        if letter in number: match +=1
                    if match == 2: sortedNumbers[2] = number
                    elif match == 3: sortedNumbers[5] = number
                    else: print('Error')                       
            case 6:
                if all((letter in number) for letter in sortedNumbers[4]):
                    sortedNumbers[9] = number
                elif all((letter in number) for letter in sortedNumbers[7]):
                    sortedNumbers[0] = number
                else: sortedNumbers[6] = number
            case 7:
                sortedNumbers[8]=number
    return sortedNumbers

def getNumber(mapTable, digits):
    result=''
    for digit in digits:
        for x in mapTable:
            if digit == x: result += str(mapTable.index(x))
    return int(result)

def sortList(a_list):
    newlist=[]
    for entry in a_list:
        newlist.append(sortAlphabetically(entry))
    return newlist

def sortAlphabetically(a_string):
    sortedList=sorted(a_string)
    sortedString = "".join(sortedList)
    return sortedString
        

#MainPart:

filename = '2021_08.txt'

datalist = list(np.loadtxt(filename, dtype=str, delimiter=' | '))
inputData = dataimport(datalist)

print('Anzahl eindeutig identifizierbarer Zahlen:', part1(inputData))
print('Summe aller 4-stelligen Zahlen:', part2(inputData))
