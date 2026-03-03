'''
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the 
root node down to the nearest leaf node. Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root and root.left == None:
            return self.minDepth(root.right) +1
        if root and root.right == None:
            return self.minDepth(root.left) + 1
        
        leftDepth = self.minDepth(root.left) + 1
        rightDepth = self.minDepth(root.right) + 1
        return min(leftDepth, rightDepth)