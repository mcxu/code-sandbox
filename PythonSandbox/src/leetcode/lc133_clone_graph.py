class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        newNode = Node(node.val)
        visited = set()
        self.graphDfs(node, visited, newNode)
        return newNode


    def graphDfs(self, node, visited, newNode):
        if node == None:
            return 
        
        print("current node: ", node.val)
        print("visited: ", visited)
        if node.val not in visited:
            visited.add(node.val)
            newNode.neighbors.append(Node(node.val))
            print("newNode added: ", [n.val for n in newNode.neighbors])
                
        for _,neighbor in enumerate(node.neighbors):
            if neighbor not in visited:
                self.graphDfs(neighbor, visited, newNode.neighbors[-1])