class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        lowerLim = -float('inf')
        upperLim = float('inf')
        validBst = self.validateBst(root, lowerLim, upperLim)
        return validBst
    
    def validateBst(self, root, lowerLim, upperLim):
        if root == None:
            return True
        
        if root.val <= lowerLim or root.val >= upperLim:
            return False
        
        isLeftValid = self.validateBst(root.left, lowerLim, root.val)
        isRightValid = self.validateBst(root.right, root.val, upperLim)
        return isLeftValid & isRightValid
    

