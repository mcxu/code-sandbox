'''
Graph search using adjacency list
'''
class GraphSearchAdjList:
    def dfsAdjListIterative(self, adjList):
        if not adjList:
            return []
        
        result= [0]
        stack = [0]
        visited=set(stack)
        while stack:
            currNode = stack[-1]
            if currNode not in visited:
                visited.add(currNode)
                result.append(currNode)
            connections = []
            for toNode in adjList[currNode]:
                if toNode not in visited:
                    connections.append(toNode)
                    break
            if not connections:
                stack.pop()
            else:
                stack += connections
        return result
    # ============================================================

    def dfsAdjListRecursive(self, adjList):
        result = []
        visited = set()
        self.dfsAdjListHelper(adjList, 0, result, visited)
        return result

    def dfsAdjListHelper(self, adjList, currNode, result, visited):
        if currNode not in visited:
            visited.add(currNode)
            result.append(currNode)

        for _,connectedNode in enumerate(adjList[currNode]):
            if connectedNode not in visited:
                self.dfsAdjListHelper(adjList, connectedNode, result, visited)

    # ============================================================
    
    def bfsAdjListIterative(self, adjList):
        result = []
        visited = set()
        q = [0]
        while q:
            currNode = q.pop()
            if currNode not in visited:
                visited.add(currNode)
                result.append(currNode)
            for _,connectedNode in enumerate(adjList[currNode]):
                if connectedNode not in visited:
                    q.insert(0,connectedNode)
            #print("q now: ", q)
        return result


    # ============================================================

    def bfsAdjListRecursive(self, adjList):
        result = []
        visited = set()
        q = [0]
        self.bfsAdjListHelper(adjList, q, result, visited)
        return result

    def bfsAdjListHelper(self, adjList, q, result, visited):
        if not q:
            return
        currNode = q.pop()
        if currNode not in visited:
            visited.add(currNode)
            result.append(currNode)
        for _,connectedNode in enumerate(adjList[currNode]):
            q.insert(0, connectedNode)
        self.bfsAdjListHelper(adjList, q, result, visited)
    
    # ============================================================

    def buildAdjList(self, n, edges):
        adjList = {}
        for i in range(n):
            adjList[i] = []
            for j,e in enumerate(edges):
                if i==e[0]:
                    adjList[i].append(e[1])
        return adjList

    def adjList1(self):
        # from here: https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/ 
        # Expected DFS output: [0, 1, 4, 5, 2, 3, 6]
        # Expected BFS output: [0, 1, 2, 4, 5, 3, 6]
        n = 7
        edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
        al = self.buildAdjList(n,edges)
        for l in al.keys():
            print("{}:{}".format(l, al[l]))
        return al
    
    def adjList2(self):
        # from here: https://thecodingsimplified.com/depth-first-search-dfs-on-graph-with-implementation/
        # Expected DFS output: [0, 1, 2, 3, 4, 5]
        # Expected BFS output: [0, 1, 3, 2, 4, 5]
        n = 6
        edges = [[0,1],[1,2],[0,3],[3,4],[4,5],[1,3]]
        al = self.buildAdjList(n,edges)
        for l in al.keys():
            print("{}:{}".format(l, al[l]))
        return al

    def test_dfsAdjListIterative(self, al):
        print("test_dfsAdjListIterative")
        res = self.dfsAdjListIterative(al)
        print("res: ", res)
    
    def test_dfsAdjListRecursive(self, al):
        print("test_dfsAdjListRecursive")
        res = self.dfsAdjListRecursive(al)
        print("res: ", res)
    
    def test_bfsAdjListIterative(self, al):
        print("test_bfsAdjListIterative")
        res = self.bfsAdjListIterative(al)
        print("res: ", res)

    def test_bfsAdjListRecursive(self, al):
        print("test_bfsAdjListRecursive")
        res = self.bfsAdjListRecursive(al)
        print("res: ", res)

gs = GraphSearchAdjList()
al = gs.adjList1()
#al = gs.adjList2()
#gs.test_dfsAdjListIterative(al)
#gs.test_dfsAdjListRecursive(al)
#gs.test_bfsAdjListIterative(al)
gs.test_bfsAdjListRecursive(al)