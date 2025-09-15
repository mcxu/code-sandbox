class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)

    def helper(self, root):
        if root == None:
            return 0
        
        leftDepth = 1 + self.helper(root.left)
        rightDepth = 1 + self.helper(root.right)
        return max(leftDepth, rightDepth)