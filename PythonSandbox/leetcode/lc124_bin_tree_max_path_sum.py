# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mps = [-float('inf')] # max path sum, stored in an array so we have a mutable reference
        self.getMpsSegment(root, mps)
        return mps[0]
    
    #postorder traversal
    def getMpsSegment(self, root, mps):
        if root == None:
            return 0
        
        # the 0 keeps the lower bound at 0, therefore excluding negative numbers
        # mpsLeft and mpsRight do not include the CURRENT root
        mpsLeft = max(0, self.getMpsSegment(root.left, mps))
        mpsRight = max(0, self.getMpsSegment(root.right, mps))
        
        # max path sum including the CURRENT root
        mpsRoot = mpsLeft + root.val + mpsRight
        mps[0] = max(mps[0], mpsRoot)

        # return max path segment only, left or right, not both
        mpsSegment = max(mpsLeft, mpsRight) + root.val
        return mpsSegment
        