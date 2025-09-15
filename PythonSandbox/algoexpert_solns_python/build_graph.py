'''
build a graph in multiple ways
Using the graph from here for testing: https://www.baeldung.com/cs/cycles-undirected-graph
'''
import time

class Node:
    def __init__(self, val, connections = None):
        self.val = val
        self.connections = connections if connections is not None else []

    def __repr__(self):
        return(f"(val:{self.val}, connections:{[x.val for x in self.connections]})")

class BuildGraph:
    # Build object representation of graph from an adjacency list using iterative DFS
    def buildGraphGivenAdjList_iterativeDFS(self, adjList):
        
        minVal = min(adjList.keys())

        # using iterative DFS
        stack = [minVal] 
        graphMap = {}
        visited = set()

        while stack:
            currVal = stack.pop()
            
            if currVal not in visited:
                visited.add(currVal)

                currNewNode = Node(currVal)
                graphMap[currVal] = currNewNode
                
                for neighborVal in adjList[currVal]:
                    newNeighborNode = None
                    
                    if neighborVal not in visited:
                        stack.append(neighborVal)
                        newNeighborNode = Node(neighborVal)
                        graphMap[neighborVal] = newNeighborNode
                    else:
                        newNeighborNode = graphMap[neighborVal]

                    currNewNode.connections.append(newNeighborNode)

        return graphMap

    # build object representation of graph from an adjacency list using recursive DFS
    def buildGraphGivenAdjList_recursiveDFS(self, adjList):

        def dfs(currVal, adjList, graphMap, visited):
            if currVal not in visited:
                visited.add(currVal)

                currNewNode = Node(currVal)
                graphMap[currVal] = currNewNode

                for neighborVal in adjList[currVal]:
                    newNeighborNode = None

                    if neighborVal not in visited:
                        newNeighborNode = Node(neighborVal)
                        graphMap[neighborVal] = newNeighborNode
                    else:
                        newNeighborNode = graphMap[neighborVal]
                    
                    currNewNode.connections.append(newNeighborNode)

                    # make recursive call
                    dfs(neighborVal, adjList, graphMap, visited)

        visited = set()
        minVal = min(adjList.keys())
        graphMap = {}
        dfs(minVal, adjList, graphMap, visited)
        return graphMap

    def printGraphDFS(self, graphMap):
        
        def dfs(currVal, visited, traversedValues):
            # print("----- currVal: ", currVal)
            # print("traversedValues: ", traversedValues)

            if currVal not in visited:
                visited.add(currVal)
                traversedValues.append(currVal)

            for connectionNode in graphMap[currVal].connections:
                # print("connectionNode: ", connectionNode)
                # time.sleep(1)
                if connectionNode.val not in visited:
                    dfs(connectionNode.val, visited, traversedValues)
            return
        
        print('In printGraphDFS: ', graphMap)
        currVal = min(graphMap.keys())
        visited = set()
        traversedValues = []
        print("getting graph values")
        dfs(currVal, visited, traversedValues)
        return traversedValues

    def test_buildGraphGivenAdjList(self):
        # adjList = {
        #     1: [2,4],
        #     2: [1,3],
        #     3: [2,4],
        #     4: [1,3]
        # }

        adjList = {
            1: [2],
            2: [1,3],
            3: [2,4,6],
            4: [3,5],
            5: [4,6],
            6: [5,3]
        }

        # graphMap = self.buildGraphGivenAdjList_iterativeDFS(adjList)
        graphMap = self.buildGraphGivenAdjList_recursiveDFS(adjList)
        print("returned graphMap: ", graphMap)
        graphValues = self.printGraphDFS(graphMap)
        print("graphValues: ", graphValues)

bg = BuildGraph()
bg.test_buildGraphGivenAdjList()