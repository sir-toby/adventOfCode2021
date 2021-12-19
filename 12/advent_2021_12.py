
import numpy as np
import pdb

def getEdges(inputFile):
    edgeList = []
    for element in inputFile:
        tupel = element.split('-')
        edgeList.append(tupel.copy())
        tupel.reverse()
        edgeList.append(tupel.copy())
    return edgeList    

def findEdgesWith1(currentNode, visited, goodPaths, badPaths, edges):
    goodEdges = []
    for edge in edges:
        if (edge[0] == currentNode and not (
            (edge[1][0].islower() == True and edge[1] in visited) or
            (edge[1] == 'end' and (visited + ['end']) in goodPaths) or
            (visited + [edge[1]] in badPaths)
            )):
            goodEdges.append(edge)
    return list(goodEdges)

def findEdgesWith2(currentNode, visited, goodPaths, badPaths, edges):
    goodEdges = []
    smallVisitedTwice = False
    seen = []
    
    for e in visited:
        if e[0].islower() and e in seen:
            smallVisitedTwice = True
        else: seen.append(e)
    
    for edge in edges:
        if (edge[0] == currentNode and not (
            (edge[1] == 'start') or                                   #do not go back to start
            (visited + [edge[1]] in goodPaths) or                     #do not go back to finished paths
            (visited + [edge[1]] in badPaths) or                    #do not go back to unfinishable paths
            (edge[1][0].islower() == True and edge[1] in visited and smallVisitedTwice == True)   
            )):
            goodEdges.append(edge)
    return list(goodEdges)


# Main Part
filename = '2021_12.txt'

inputFile = list(np.loadtxt(filename, dtype=str))
edges = getEdges(inputFile)

visited = ['start']
goodPaths = []
badPaths = []

while len(visited) != 0:
    currentNode = visited[-1]
    
    if currentNode == 'end':
        goodPaths.append(visited.copy())
        visited.pop()
    else:
        reachableEdges = findEdgesWith2(currentNode, visited, goodPaths, badPaths, edges)
    
        if len(reachableEdges) == 0:
            if currentNode == 'start':
                visited.pop()
            else:
                badPaths.append(visited.copy())
                visited.pop()

        else:
            firstToVisit = reachableEdges[0]
            visited.append(firstToVisit[1])

print(len(goodPaths))   
