'''
Detect a cycle in an undirected graph. Return true if there exists a cycle, false otherwise.
https://www.baeldung.com/cs/cycles-undirected-graph 
https://www.techiedelight.com/check-undirected-graph-contains-cycle-not/ 
'''
# import time

class Solution:
    def cycleExistsInGraph(self, adjList):
        if adjList == None:
            return False

        visited = set()
        startNode = 0 # starting vertex
        parent = None
        result = self.detectCycle(startNode, adjList, visited, parent)
        return result
    
    def detectCycle(self, node, adjList, visited, parent):
        print(f"--- detectCycle: node:{node}, visited:{visited}, parent:{parent}")

        if node not in visited:
            visited.add(node)
        print("visited after adding: ", visited)
        for neighbor in adjList[node]:
            print("neighbor: ", neighbor)
            # if neighbor has already been visited
            if neighbor in visited:
                print("neighbor in visited")
                if neighbor != parent:
                    print("neighbor != parent")
                    return True
            # if neighbor was not visited before
            else:
                print("neighbor NOT in visited")
                resultForNeighbor = self.detectCycle(neighbor, adjList, visited, node)
                if resultForNeighbor == True:
                    return True 
        
        return False

    # ------------- utils ---------------

    def createAdjListFromEdges(self, edges):
        adjList = {}

        for edge in edges:
            frm, to = edge[0], edge[1]

            # one direction
            if frm in adjList:
                adjList[frm].append(to)
            else:
                adjList[frm] = [to]
            
            # account for other direction
            if to in adjList:
                adjList[to].append(frm)
            else:
                adjList[to] = [frm]
        
        return adjList

    # -----------------------------------

    def test1(self):
        adjList = {
            0: [1,2],
            1: [0,2],
            2: [0,1,3],
            3: [2]
        }
        expected = True

        result = self.cycleExistsInGraph(adjList)
        print("result: ", result)

    def test2(self):
        # List of graph edges
        edges = [
            (0, 1), (0, 6), (0, 7), (1, 2), (1, 5), (2, 3),
            (2, 4), (7, 8), (7, 11), (8, 9), (8, 10), (10, 11)
            # edge (10, 11) introduces a cycle in the graph
        ]

        adjList = self.createAdjListFromEdges(edges)
        print("adjList: ", adjList)

        expected = True

        result = self.cycleExistsInGraph(adjList)
        print("result: ", result)


s = Solution()
# s.test1()
s.test2()