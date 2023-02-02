"""
https://leetcode.com/problems/house-robber-iii/description/ 
"""
from ..utils.binary_tree_utils import BinaryTreeUtils as btu

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(arr):
    if not arr:
        return None

    def h(arr, i):
        if i > len(arr)-1:
            return None
        if arr[i]==None:
            return None
        
        root = TreeNode(arr[i])
        print("node created: ", root.val)
        root.left = h(arr, 2*i+1)
        root.right = h(arr, 2*i+2)
        return root
    
    root = h(arr, 0)
    return root

class Solution:
    def rob(self, root: TreeNode) -> int:
        rewardFromPickingRoot = self.getReward(root, True, {}) # separate memos because these are treated as 2 separate calls
        rewardFromSkippingRoot = self.getReward(root, False, {})
        return max(rewardFromPickingRoot, rewardFromSkippingRoot)

    # @lru_cache()
    def getReward(self, root, includeValAtNode, memo):
        if root == None:
            return 0

        # print(f"====== root: {id(root)}, value: {root.val}")
        print(f"memo: ", memo)
        key = (id(root), includeValAtNode)
        if key in memo.keys():
            return memo[key]

        rewardFromThisNode = 0
        if includeValAtNode:
            rewardFromThisNode = root.val + self.getReward(root.left, False, memo) + self.getReward(root.right, False, memo)
            # print("rewardFromPickingCurrNode: ", rewardFromThisNode)
        else:
            rewardFromPickLeft = self.getReward(root.left, True, memo)
            rewardFromSkipLeft = self.getReward(root.left, False, memo)
            rewardFromPickRight = self.getReward(root.right, True, memo)
            rewardFromSkipRight = self.getReward(root.right, False, memo)

            maxRewardFromLeft = max(rewardFromPickLeft, rewardFromSkipLeft)
            maxRewardFromRight = max(rewardFromPickRight, rewardFromSkipRight)
            rewardFromThisNode = maxRewardFromLeft + maxRewardFromRight
        
        memo[key] = rewardFromThisNode
        return rewardFromThisNode

    def test(self):
        cases = [
            # dict(arr=[3,2,3,None,3,None,1], expected=7),
            # dict(arr=[3,4,5,1,3,None,1], expected=9),
            dict(arr=[2,1,3,None,4], expected=7),
        ]

        for case in cases:
            print("case: ", case)
            root = btu.buildTree(case["arr"])
            res = self.rob(root)
            print("res: ", res)
            assert res == case["expected"]

sol = Solution()
sol.test()
