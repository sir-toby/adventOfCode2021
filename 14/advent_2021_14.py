import numpy as np
import pdb

def importFile(fileName):
    file = open(fileName, mode='r')
    text = file.read()
    startPolymer = text[:text.find('\n\n')]
    rules = text[text.find('\n\n')+2:]
    rules = rules.split('\n')
    newRules = []
    for rule in rules:
        new = rule.split(' -> ')
        new[1] = new[0][0] + new[1] + new[0][1]
        newRules.append(new)
    return startPolymer, newRules

def prolongation(polymer, rules):
    newPolymer = ''
    for i in range(len(polymer)-1):
        elements = polymer[i:i+2]
        for rule in rules:
            if elements == rule[0]:
                newPolymer = newPolymer[:-1]
                newPolymer += rule[1]
    return newPolymer

def counting(polymer):
    counts = {}
    for e in polymer:
        if e in counts:
            counts[e] += 1
        else: counts[e] = 1
    allValues = counts.values()
    result = max(allValues)-min(allValues)
    return result
   


##Main Part:

fileName = '2021_14.txt'
numberOfSteps = 15

startPolymer, rules = importFile(fileName)

polymer = startPolymer
for i in range(0, numberOfSteps):
    polymer = prolongation(polymer, rules)

print(counting(polymer))

    

