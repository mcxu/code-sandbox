'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left= None
        self.right=None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        ancestor = [root.val]
        self.dfs(root, p, q, ancestor)
        return ancestor[0]

    def dfs(self, root, p, q, ancestor):
        if root == None:
            return False

        leftContainsVal = self.dfs(root.left, p, q, ancestor)
        rightContainsVal = self.dfs(root.right, p, q, ancestor)
        
        common = False
        if root.val==p or root.val==q:
            common = True
        
        if common + leftContainsVal + rightContainsVal >= 2:
            ancestor[0] = root.val
        
        return common or leftContainsVal or rightContainsVal

