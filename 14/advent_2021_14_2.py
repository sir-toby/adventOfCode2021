import numpy as np
import pdb

def importFile(fileName):
    file = open(fileName, mode='r')
    text = file.read()
    startPolymer = text[:text.find('\n\n')]
    polymerList = {}
    counts = {}
    for i in range(len(startPolymer)-1):
        elements = startPolymer[i:i+2]
        if elements in polymerList:
            polymerList[elements] += 1
        else: polymerList[elements] = 1
    for e in startPolymer:
        if e in counts:
            counts[e] += 1
        else: counts[e] = 1
    
    rules = text[text.find('\n\n')+2:]
    rules = rules.split('\n')
    newRules = {}
    for rule in rules:
        rule = rule.split(' -> ')
        new = [rule[0][0] + rule[1], rule[1] + rule[0][1], rule[1]]
        newRules[rule[0]] = new
    return polymerList, newRules, counts


def prolongation(polymer, counts, rules):
    newPolymer = polymer.copy()
    for key in polymer:
        if polymer[key] != 0:
        
            if rules[key][0] in newPolymer:
                newPolymer[rules[key][0]] += polymer[key]
            else: newPolymer[rules[key][0]] = polymer[key]
            
            if rules[key][1] in newPolymer:
                newPolymer[rules[key][1]] += polymer[key]
            else: newPolymer[rules[key][1]] = polymer[key]

            newPolymer[key] -= polymer[key]
            
            if rules[key][2] in counts:
                counts[rules[key][2]] += polymer[key]
            else: counts[rules[key][2]] = polymer[key]

    return newPolymer

def counting(polymer):
    allValues = counts.values()
    result = max(allValues)-min(allValues)
    valueSum = sum(allValues)
    return result, valueSum 

##Main Part:

fileName = '2021_14.txt'
numberOfSteps = 40

polymer, rules, counts = importFile(fileName)

for i in range(0, numberOfSteps):
    polymer = prolongation(polymer, counts, rules)

print(counting(polymer))
