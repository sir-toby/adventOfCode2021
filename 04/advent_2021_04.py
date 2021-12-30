import numpy as np
import pdb

def getNumbers(filename):
    inputFile = open(filename, mode='r')
    text = inputFile.read()

    drawNumbers = text[:text.find('\n')] + ','
    numbers=[]
    j=0
    for i in range(len(drawNumbers)):
        if drawNumbers[i]==',':
            numbers.append(drawNumbers[j:i])
            j=i+1
    return numbers

def getMatrixList(filename):
    inputFile = open(filename, mode='r')
    text = inputFile.read()

    matrixText = text[text.find('\n\n')+2:] + '\n\n'
    matricesplain = []
    matrices = []
    matrices2 = []
    matrix = []
    j=0
    
    for i in range(len(matrixText)):
        if matrixText[i:i+2] == '\n\n':
            matricesplain.append(matrixText[j:i])
            j=i+2

    for mat in matricesplain:
        matrix = getMatrix(mat)
        matrices.append(matrix)

    for matrix in matrices:
        if len(matrix)==5:
            matrices2.append(matrix)
        else:
            print('Gelöschte Elemente:', matrix)
    print(matrices2)
    return matrices2

def getMatrix(mat):
    line = []
    lines = []
    matrix = []
    cell = []
    j = 0
    k = 0
    mat += '\n'
    for i in range(len(mat)):
        if mat[i]=='\n':
            lines.append(mat[j:i] + ' ')
            j = i+1
            k += 1

    for line in lines:
        j=0
        cell=[]
        line = line.replace('  ', ' ')
        if line[0] == ' ': line = line[1:]
        for l in range(len(line)):
            if line[l] == ' ':
                cell.append(line[j:l])
                j = l+1
        matrix.append(cell)
    return matrix

def transposeList(matrixListInput):
    transposed = []
    transposedList = []
    for matrix in matrixListInput:
        transposed.append(list(zip(*matrix)))
    for matrix in transposed:
        matrixList = []
        for line in matrix:
            matrixList.append(list(line))
        transposedList.append(matrixList)                
    return transposedList

def transposeMatrix(matrix):
    transposed = list(zip(*matrix))
    matrixList = []
    for line in transposed:
        matrixList.append(list(line))
    return matrixList

def winningScore(number, matrix):
    summe = 0
    for line in matrix:
        for element in line:
            if element != 'x':
                summe += int(element)
    return (summe*int(number))
        
def determineWinning(numbers, listOfMatrices):

    summe = 0
    for number in numbers:
        for matrix in listOfMatrices:
            for line in matrix:
                if number in line:
                    line[line.index(number)] = 'x'
        for matrix in listOfMatrices:
            for line in matrix:
                if line == ['x']*5:
                    return winningScore(number, matrix)
            for line in transposeMatrix(matrix):
                 if line == ['x']*5:
                    return winningScore(number, matrix)

def determineLosing(numbers, listOfMatrices):
    for number in numbers:
        for matrix in listOfMatrices:
            listOfMatrices2 = listOfMatrices
            for line in matrix:
                if number in line:
                    line[line.index(number)] = 'x'
        for matrix in listOfMatrices:
            for line in matrix:
                if line == ['x']*5:
                    if len(listOfMatrices) == 1:
                        return winningScore(number, matrix)
                    try: listOfMatrices2.remove(matrix)
                    except: continue
            for line in transposeMatrix(matrix):
                if line == ['x']*5:
                    if len(listOfMatrices) == 1:
                        return winningScore(number, matrix)
                    try: listOfMatrices2.remove(matrix)
                    except: continue
        listOfMatrices = listOfMatrices2


filename = 'C:\\Users\\tbachmann\\Desktop\\Advent of coding\\2021_4.txt'

numbers = getNumbers(filename)
matrices = getMatrixList(filename)
matricesTransposed = transposeList(matrices)


print('Winning Bingo number: ', determineWinning(numbers, matrices))
print('Losing Bingo number: ', determineLosing(numbers, matrices))
