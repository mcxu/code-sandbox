# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # BFS 
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