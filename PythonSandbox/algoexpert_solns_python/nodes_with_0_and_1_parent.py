# https://www.glassdoor.com/Interview/Karat-Software-Engineering-Manager-Interview-Questions-EI_IE1286154.0,5_KO6,34.htm#InterviewReview_35124106
'''
Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:

1 2 4
 \ / / | \
  3 5 8 9
   \ / \ \
    6 7 11

Sample input/output (pseudodata):

parentChildPairs = [
    (1, 3), (2, 3), (3, 6), (5, 6),
    (5, 7), (4, 5), (4, 8), (4, 9), (9, 11)
]

Write a function that takes this data as input and returns two collections: 
one containing all individuals with zero known parents, 
and one containing all individuals with exactly one known parent.

Output may be in any order:

findNodesWithZeroAndOneParents(parentChildPairs) => [
  [1, 2, 4], // Individuals with zero parents
  [5, 7, 8, 9, 11] // Individuals with exactly one parent
]

n: number of pairs in the input  
'''

# pairs constitute a graph, so create adjacency list
def createAdjList(pairs):
    adjList = {}

    for i,p in enumerate(pairs):
        fr=p[0]; to=p[1]
        if fr in adjList.keys():
            adjList[fr].append(to)
        else:
            adjList[fr] = [to]
    return adjList

def findRoots(adjList):
    valList = []
    for v in adjList.values():
        valList += v
    toSet = set(valList)
    roots = []
    for k in adjList.keys():
        if k not in toSet:
            roots.append(k)
    return roots

def findNodesWith1Parent(adjList):
    valList = []
    for v in adjList.values():
        valList += v
    
    nodesWith1Parent = set()
    moreThan1Parent = set()
    for v in valList:
        if v not in nodesWith1Parent:
            if v not in moreThan1Parent:
                nodesWith1Parent.add(v)
        else:
            moreThan1Parent.add(v)
            nodesWith1Parent.remove(v)

    return list(nodesWith1Parent)

def findCollections(adjList):
    roots = findRoots(adjList)
    #print("roots: ", roots)

    singleParentNodes = findNodesWith1Parent(adjList)
    #print("singleParentNodes: ", singleParentNodes)

    return  {
        "roots" : roots, 
        "singleParentNodes" : singleParentNodes}

parentChildPairs = [
    (1, 3), (2, 3), (3, 6), (5, 6),
    (5, 7), (4, 5), (4, 8), (4, 9), (9, 11)
]
adjList = createAdjList(parentChildPairs)
res = findCollections(adjList)
print("res: ", res)