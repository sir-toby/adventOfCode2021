import numpy as np
import pdb

def rollDeterministicDie(i):
    score = (3*i+1 + 3*i+2 + 3*i+3)%100
    return score

# Main Part

##pos1 = 8
##pos2 = 2
pos1 = 4
pos2 = 8
score1 = 0
score2 = 0
count = 0

#part1:
while score1<1000 and score2<1000:
    #Player1:
    diceSum1 = rollDeterministicDie(count)
    pos1 = (pos1+diceSum1)%10
    if pos1 == 0: score1 += 10
    else: score1 += pos1
    count += 1
    if score1>=1000: break
    #Player2:
    diceSum2 = rollDeterministicDie(count)
    pos2 = (pos2+diceSum2)%10
    if pos2 == 0: score2 += 10
    else: score2 += pos2    
    count += 1

if score1>=1000: loseScore = score2*count*3
if score2>=1000: loseScore = score1*count*3

print('Part 1:', loseScore)

#part2:

#maimum number of possible throws: 9 (2+1+4+2+1+4+2+1+4; 1+4+1+4+1+4+1+4+1)
#paths = {path: [position, score, amount]}

def oneThrow(paths):
    diceRoll = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    wincount = 0
    nowincount = 0
    newPaths = {}
    for path in paths:
        for roll in diceRoll:
            position = (paths[path][0] + int(roll))%10
            key = str(path)+str(position)
            if position == 0: score = paths[path][1] + 10
            else: score = paths[path][1] + position
            amount = paths[path][2]*int(diceRoll[roll])
            if score >= 21:
                wincount += amount
            else:
                nowincount += amount
                newPaths[key] = [position, score, amount]
    return newPaths, wincount, nowincount

def twoPlayers(start1, start2):
    paths1 = {start1: [start1, 0, 1]}
    paths2 = {start2: [start2, 0, 1]}
    winAll1 = 0
    winAll2 = 0
    nowin1 = 0
    nowin2 = 0
    while paths1 != {} and paths2 != {}:
        #breakpoint()
        paths1, win1, nowin1 = oneThrow(paths1)
        winAll1 += win1*nowin2
        paths2, win2, nowin2 = oneThrow(paths2)
        winAll2 += win2*nowin1
    return winAll1, winAll2

#main part:
wins1, wins2 = twoPlayers(8, 2)
print('Part 2:', max(wins1, wins2))


