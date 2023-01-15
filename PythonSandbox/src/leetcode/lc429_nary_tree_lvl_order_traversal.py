'''
https://leetcode.com/problems/n-ary-tree-level-order-traversal/
'''
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> [[int]]:
        levelMap = {}
        d = 0
        self.helper(root, levelMap, d)
        out = []
        for k in sorted(levelMap.keys()):
            out.append(levelMap[k])
        return out
    
    def helper(self, root, levelMap, d):
        if root == None:
            return
        
        if d in levelMap.keys():
            levelMap[d].append(root.val)
        else:
            levelMap[d] = [root.val]
        
        for c in root.children:
            self.helper(c, levelMap, d+1)
        