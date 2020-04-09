'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        levelMap = {}
        self.helper(root, 0, levelMap)
        #print("levelMap after: ", levelMap)
        output = []
        i = 0
        while i in levelMap.keys():
            output.append(levelMap[i])
            i += 1
        return output
    
    def helper(self, root, depth, levelMap):
        if root == None:
            return
        
        if depth in levelMap.keys():
            if depth % 2 == 0:
                levelMap[depth].append(root.val)
            else:
                levelMap[depth].insert(0, root.val)
        else:
            levelMap[depth] = [root.val]
            
        self.helper(root.left, depth+1, levelMap)
        self.helper(root.right, depth+1, levelMap)