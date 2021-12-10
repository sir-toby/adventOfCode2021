import numpy as np

def analyzeLines(syntax):
    errorSum = 0
    completionSum = []
    for line in syntax:
        incomplete, errorValue, completionValue = lineResult(line)
        errorSum += errorValue
        if incomplete == True: completionSum.append(completionValue)
        completionSum.sort()
        len(completionSum)
        
    return errorSum, completionSum[int((len(completionSum)-1)/2)]

def lineResult(row):
    openChars = ('(', '[', '{', '<')
    closeChars = (')', ']', '}', '>')
    chunk = []
    for char in row:
        if char in openChars:
            chunk.append((openChars.index(char)))
        elif char in closeChars:
            if chunk[-1] == closeChars.index(char):
                del chunk[-1]
            else:
                return(False, calculateError1(char), 0)
    return(True, 0, requiredForClosing(chunk))

def calculateError1(symbol):
    match symbol:
        case ')': return 3
        case ']': return 57
        case '}': return 1197
        case '>': return 25137

def requiredForClosing(remaining):
    points = 0
    for i in range(len(remaining)-1, -1, -1):
        points = points*5
        points +=remaining[i]+1
    return points


#MainPart:
filename = '2021_10.txt'
data = list(np.loadtxt(filename, dtype=str))

part1, part2 = analyzeLines(data)

print('Sum of errors for part 1:', part1, '\nMiddle value for part2:', part2)
