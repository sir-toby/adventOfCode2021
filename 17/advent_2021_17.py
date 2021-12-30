import numpy as np
import pdb



# Main Part

xMin = 57
xMax = 116
yMin = -198
yMax = -148

##xMin = 20
##xMax = 30
##yMin = -10
##yMax = -5


yIni = 1000
xIni = 1

maximum = 0
possibleVelocities = []
for y in range(yIni, yMin-1, -1):
    for x in range(xIni, xMax+1):
        maxHeight = 0
        pos = [0,0]
        xVel = x
        yVel = y
        while True:
            pos[0] += xVel
            pos[1] += yVel
            if xVel > 0: xVel -= 1
            yVel -= 1
            if pos[1] > maxHeight: maxHeight = pos[1]
            if pos[0] > xMax: break
            if pos[1] < yMin: break
            if (pos[0] <= xMax and pos[0] >= xMin) and (pos[1] <= yMax and pos[1] >= yMin):
                if maxHeight > maximum: maximum = maxHeight
                possibleVelocities.append([x, y])
                #print(x, y, maxHeight)
                break
                

print(maximum, len(possibleVelocities))
            
#VeloityComparison
fileName = 'allVelocities.txt'
file = open(fileName, mode='r')
text = file.read()
text = text.replace('\t', ' ')
text = text.split(' ')
newText = []
for e in text:
    e = e.split(',')
    e[0] = int(e[0])
    e[1] = int(e[1])
    newText.append(e)
print(sorted(newText, key=lambda x:x[1], reverse=True))

