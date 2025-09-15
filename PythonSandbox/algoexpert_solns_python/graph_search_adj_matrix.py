'''
Graph DFS and BFS using Adjacency Matrix representation of graph.
'''
class GraphSearchAdjMatrix:
    def dfsAdjMatrixIterative(self, adjMat):
        stack = []
        visited = set([0])
        result = [0]

        if adjMat:
            stack.append(0)

        while stack:
            # read node on top of stack
            currNode = stack[-1]
            if currNode not in visited:
                # mark node as visited
                visited.add(currNode)
                # append to result
                result.append(currNode)

            connections = []
            for toNode,exists in enumerate(adjMat[currNode]):
                if exists==1 and toNode not in visited:
                    connections.append(toNode)
                    break
            if not connections:
                stack.pop()
            else:
                stack += connections
            print("stack after: ", stack)
        return result

    #=============================================================================

    def dfsAdjMatrixRecursive(self, adjMat):
        output = []
        currNode = 0
        visited = set()
        self.dfsAdjMatRecHelper(adjMat, currNode, output, visited)
        return output

    def dfsAdjMatRecHelper(self, adjMat, currNode, output, visited):
        output.append(currNode)
        visited.add(currNode)
        for i,x in enumerate(adjMat[currNode]):
            if x == 1 and i not in visited:
                self.dfsAdjMatRecHelper(adjMat, i, output, visited)
            # else: # debug
            #     print("i was visited: {}, visited: {}".format(i, visited))

    #=============================================================================

    def bfsAdjMatrixIterative(self, adjMat):
        if not adjMat:
            return []
        
        out = []
        visited = set([])
        q = [0]

        while q:
            currNode = q.pop()
            if currNode not in visited:
                visited.add(currNode)
                out.append(currNode)
            for i,exists in enumerate(adjMat[currNode]):
                if exists == 1 and i not in visited:
                    q.insert(0, i)
        return out

    #=============================================================================

    def bfsAdjMatrixRecursive(self, adjMat):
        if not adjMat:
            return []

        q = [0]
        out = [q[-1]]
        visited = set([q[-1]])
        self.graphBfsAdjMatHelper(adjMat, q, visited, out)
        return out
    
    def graphBfsAdjMatHelper(self, adjMat, q, visited, out):
        if not q:
            return
        currNode = q.pop()
        if currNode not in visited:
            visited.add(currNode)
            out.append(currNode)

        for i,exists in enumerate(adjMat[currNode]):
            if exists == 1 and i not in visited:
                q.insert(0, i)
        self.graphBfsAdjMatHelper(adjMat, q, visited, out)

    #=============================================================================

    # adjadency matrix: undirected graph
    def buildAdjMatrix(self, n, edges, directed=False):
        out = [[0 for _ in range(n)] for _ in range(n)]
        for i,e in enumerate(edges):
            f = e[0]; t = e[1]
            out[f][t] = 1
            if directed == False:
                out[t][f] = 1
        return out

    def adjMatrix1(self):
        # from here: https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/ 
        # Expected DFS output: [0, 1, 4, 5, 2, 3, 6]
        # Expected BFS output: [0, 1, 2, 4, 5, 3, 6]
        n = 7
        edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
        m = self.buildAdjMatrix(n,edges,directed=False)
        for row in m:
            print(row)
        return m

    def adjMatrix2(self):
        # from here: https://thecodingsimplified.com/depth-first-search-dfs-on-graph-with-implementation/
        # Expected DFS output: [0, 1, 2, 3, 4, 5]
        # Expected BFS output: [0, 1, 3, 2, 4, 5]
        n = 6
        edges = [[0,1],[1,2],[0,3],[3,4],[4,5],[1,3]]
        m = self.buildAdjMatrix(n,edges,directed=True)
        for row in m:
            print(row)
        return m

    def test_dfsAdjMatrixIterative(self, adjm):
        result = self.dfsAdjMatrixIterative(adjm)
        print("result: ", result)
    
    def test_dfsAdjMatrixRecursive(self, adjm):
        result = self.dfsAdjMatrixRecursive(adjm)
        print("result: ", result)
    
    def test_bfsAdjMatrixIterative(self, adjm):
        print("test_bfsAdjMatrixIterative")
        result = self.bfsAdjMatrixIterative(adjm)
        print("result: ", result)

    def test_bfsAdjMatrixRecursive(self, adjm):
        print("test_bfsAdjMatrixRecursive")
        result = self.bfsAdjMatrixRecursive(adjm)
        print("result: ", result)


gs = GraphSearchAdjMatrix()
m = gs.adjMatrix1()
#m = gs.adjMatrix2()
#gs.test_dfsAdjMatrixIterative(m)
#gs.test_dfsAdjMatrixRecursive(m)
#gs.test_bfsAdjMatrixIterative(m)
gs.test_bfsAdjMatrixRecursive(m)