import numpy as np
import pdb
import copy

def importFile(fileName):
    instructions = ((open(fileName, 'r')).read()).split('\n')
    newFile = []
    for line in instructions:
        line = line.split(' ')
        if len(line) == 2: line.append([''])
        newFile.append(line)
    return newFile
    
def inp(target, number):
    variables[target] = int(number)
    return variables

def add(target, summand):
    try:
        variables[target] += int(summand)
    except:
        variables[target]+= variables[summand]
    return variables

def mul(target, factor):
    try:
        variables[target] *= int(factor)
    except:
        variables[target]*= variables[factor]
    return variables

def div(target, divisor):
    try:
        variables[target] = int(variables[target]/int(divisor))
    except:
        variables[target] = int(variables[target]/variables[divisor])
    return variables

def mod(target, divisor):
    try:
        variables[target] = variables[target]%int(divisor)
    except:
        variables[target] = variables[target]%variables[divisor]
    return variables

def eql(target, comp):
    try:
        if variables[target] == int(comp): variables[target] = 1
        else: variables[target] = 0
    except:
        if variables[target] == variables[comp]: variables[target] = 1
        else: variables[target] = 0
    return variables
    
# Main Part

fileName = '2021_24_part.txt'
instructions = importFile(fileName)

##for i in range(99999999999999, 11111111111110, -1):
##    sNo = str(i)
##    if '0' in sNo: continue
##    variables = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
##    for line in instructions:
##        match line[0]:
##            case 'inp':
##                variables = inp(line[1], sNo[0])
##                sNo = sNo[1:]
##            case 'add':
##                variables = add(line[1], line[2])
##            case 'mul':
##                variables = mul(line[1], line[2])
##            case 'div':
##                variables = div(line[1], line[2])
##            case 'mod':
##                variables = mod(line[1], line[2])
##            case 'eql':
##                variables = eql(line[1], line[2])
##        print(line, variables)
##    break
##    if i%999 == 0: print(i)
##    if variables['z'] == 0:
##        print(i)
##        break

##for i in range(11, 100):
##    sNo = str(i)
##    variables = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
##    for line in instructions:
##        match line[0]:
##            case 'inp':
##                variables = inp(line[1], sNo[0])
##                sNo = sNo[1:]
##            case 'add':
##                variables = add(line[1], line[2])
##            case 'mul':
##                variables = mul(line[1], line[2])
##            case 'div':
##                variables = div(line[1], line[2])
##            case 'mod':
##                variables = mod(line[1], line[2])
##            case 'eql':
##                variables = eql(line[1], line[2])
##    print(variables['z'])

########################
count = 0
for j in range(99969999999999, 11111111111110, -1):
    sNo = str(j)
    if '0' in sNo: continue
    count += 1
    w = 0
    x = 0
    y = 0
    z = 0
    divs = [ 1,  1,  1,  1, 26, 26,  1,  26,  1, 26,  1, 26, 26, 26]
    addx = [11, 11, 14, 11, -8, -5, 11, -13, 12, -1, 14, -5, -4, -8]
    addy = [ 1, 11,  1, 11,  2,  9,  7,  11,  6, 15,  7,  1,  8,  6]
    
    for i in range(len(sNo)):
        w = int(sNo[i])             #9,9,9,6,9,4,9,7
        if z%26+addx[i] == w: x=0   #1,1,1,1,0,1,1,0
        else: x=1                   #
        z = int(z/divs[i])          #0,10,26x1+20,26x2+10,26x2,26x1,26x1,26x1,
        z *= (25*x+1)               #0,26x,26x2,26x3,26x2,26x2, 26x2,26x1
        z += (w+addy[i])*x          #10,26x1+20,26x2+10,26x3+17,26x2,26x1+25,26x2+20,
    if count == 10000000:
        print(j)
        count = 0
    if z == 0:
        print('Result:', j)
        break
        
