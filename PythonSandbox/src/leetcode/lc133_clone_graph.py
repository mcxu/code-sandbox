class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        # iterative BFS
        q = [node]
        copyMap = {node.val: Node(node.val)}

        while q:
            currNode = q.pop(0)
            currNodeCopy = copyMap[currNode.val]

            for _,neighbor in enumerate(currNode.neighbors):
                if neighbor.val not in copyMap.keys():
                    copyMap[neighbor.val] = Node(neighbor.val)
                    q.append(neighbor)
                
                neighborCopy = copyMap[neighbor.val]
                currNodeCopy.neighbors.append(neighborCopy)

        return copyMap[node.val]