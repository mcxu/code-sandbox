'''
LC116: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
'''
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        levelMap = {}
        self.helper(root, 0, levelMap)
        
        for d in levelMap.keys():
            lvlNodes = levelMap[d]
            for i in range(len(lvlNodes)-1):
                n = lvlNodes[i]
                n.next = lvlNodes[i+1]
        return root
    
    def helper(self, root, depth, levelMap):
        if root == None:
            return
        
        if depth in levelMap.keys():
            levelMap[depth].append(root)
        else:
            levelMap[depth] = [root]
            
        self.helper(root.left, depth+1, levelMap)
        self.helper(root.right, depth+1, levelMap)