'''
Topological graph sorting
'''
class Topo:
    def topoSort(self, adjList, startNode=0):
        stack = [] #output
        visited = set()
        searchInits = [i for i in range(len(adjList))]
        # j = 0
        while searchInits:
            # print("searchInits: ", searchInits)
            currNode = searchInits[0]
            print("currNode: ", currNode)
            # if j==0 and startNode != 0:
            #     currNode = startNode
            searchInits.remove(currNode)
            if currNode not in visited:
                self.topoDFS(adjList, currNode, stack, visited)
            # j += 1
        return stack
    
    def topoDFS(self, adjList, currNode, stack, visited):
        visited.add(currNode)
        for _,connectedNode in enumerate(adjList[currNode]):
            if connectedNode not in visited:
                self.topoDFS(adjList, connectedNode, stack, visited)
        stack.append(currNode)

    def buildAdjList(self, n, edges):
        adjList = {}
        for i in range(n):
            adjList[i] = []
            for j,e in enumerate(edges):
                if i==e[0]:
                    adjList[i].append(e[1])
        return adjList
    
    def adjList1(self):
        # https://www.youtube.com/watch?v=ddTC4Zovtbc&t=462s
        n = 7
        edges = [[0,2],[1,2],[1,4],[2,3],[3,5],[5,6],[4,5]]
        adjList = self.buildAdjList(n,edges)
        print("adjList: ", adjList)
        return adjList
    
    def adjList2(self):
        # https://youtu.be/eL-KzMXSXXI?t=375
        n = 13
        edges = [[2,0],[2,1],[0,3],[1,3],[4,0],[4,3],[3,6],[3,7],[4,5],[5,10],[6,8],[7,9],[7,8],[5,9],[8,11],[9,11],[9,12],[10,9]]
        adjList = self.buildAdjList(n,edges)
        print("adjList: ", adjList)
        return adjList

    def test_topoSort1(self):
        adjList = self.adjList1()
        res = self.topoSort(adjList, startNode=0)
        print("res: ", res)

    def test_topoSort2(self):
        adjList = self.adjList2()
        res = self.topoSort(adjList, startNode=7)
        print("res: ", res)

t = Topo()
#al = t.adjList1()
#al = t.adjList2()
t.test_topoSort1()
#t.test_topoSort2()