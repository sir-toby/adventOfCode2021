import numpy as np
import pdb

global debug
debug=False

def add(summand1, summand2):
    snailSum = '[' + summand1 + ',' + summand2 + ']'
    return snailSum

def checkExplosion(number):
    depth = 0
    for i in range(len(number)):
        if number[i] == '[':
            depth += 1
            if depth == 5: return i
        elif number[i] == ']':
            depth -= 1
    return False

def explode(number, pos):
    pos2 = number.find(']', pos)
    pair = (number[pos+1:pos2]).split(',')
    for i in range(pos, 0, -1):
        if number[i].isnumeric():
            if number[i-1].isnumeric():
                added = int(number[i-1:i+1])+int(pair[0])
                number = number[:i-1] + str(added) + number[i+1:] 
            else:
                added = int(number[i])+int(pair[0])
                number = number[:i] + str(added) + number[i+1:]
                if added > 9:
                    pos += 1
                    pos2 += 1
            break
    for i in range(pos2, len(number)):
        if number[i].isnumeric():
            if number[i+1].isnumeric():
                added = int(number[i:i+2])+int(pair[1])
                number = number[:i] + str(added) + number[i+2:]
            else:
                added = int(number[i])+int(pair[1])
                number = number[:i] + str(added) + number[i+1:]
            break
            #if added > 9: pos += 1
    number = number[:pos]+'0'+number[pos2+1:]
    return number

def checkReduce(number):
    for i in range(len(number)):
        if number[i:i+2].isnumeric(): return i
    return False

def reduce(number, pos):
    toReduce = int(number[pos:pos+2])
    if toReduce%2 == 0:
        new = '['+str(int(toReduce/2))+','+str(int(toReduce/2))+']'
    else:
        new = '['+str(int(toReduce/2-0.5))+','+str(int(toReduce/2+0.5))+']'
    number = number[:pos] + new + number[pos+2:]
    return number


def magnitude(number):
    while number.isnumeric() == False:
        #breakpoint()
        pos2 = number.find(']')
        for i in range(pos2, -1, -1):
            if number[i] == '[':
                pos1 = i
                break
        pair = (number[pos1+1:pos2]).split(',')
        mag = 3*int(pair[0])+2*int(pair[1])
        number = number[:pos1]+str(mag)+number[pos2+1:]
    return int(number)
        

# Main Part

fileName = '2021_18.txt'
file = open(fileName, mode='r')
summands = (file.read()).split('\n')

#part1:
snailSum = summands[0]
summands = summands[1:]
for summand in summands:
    temp = add(snailSum, summand)
    while checkExplosion(temp) != False or checkReduce(temp) != False:
        if checkExplosion(temp) != False:
            temp = explode(temp, checkExplosion(temp))
            continue
        if checkReduce != False:
            temp = reduce(temp, checkReduce(temp))
    snailSum = temp
print(snailSum)
print(magnitude(snailSum))


#part2:
maximum = 0
for summand in summands:
    for summand2 in summands:
        if summand == summand2: continue
        temp = add(summand, summand2)
        while checkExplosion(temp) != False or checkReduce(temp) != False:
            if checkExplosion(temp) != False:
                temp = explode(temp, checkExplosion(temp))
                continue
            if checkReduce != False:
                temp = reduce(temp, checkReduce(temp))
        if magnitude(temp)>maximum: maximum = magnitude(temp)
print(maximum)
         


