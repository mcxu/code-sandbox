'''
987. Vertical Order Traversal of a Binary Tree
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

Given binary tree, return vertical order traversal. This means that
from root node, the vertical line is x=0, left child is on line x=-1,
right child is on line x=1, and so on.

Example 1:
Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

Example 2:
Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode):
        def helper(root, x, y, memo):
            nonlocal treeDepth
            if root is None:
                return 
            
            if x not in memo.keys():
                memo[x] = [[] for _ in range(treeDepth)]
                memo[x][y].append(root.val)
            else:
                memo[x][y].append(root.val)

            helper(root.left, x-1, y+1, memo)
            helper(root.right, x+1, y+1, memo)

        treeDepth = self.getDepth(root)
        memo = {}
        helper(root, 0, 0, memo) # x:0, y:0
        
        # print("memo after")
        # for key in memo.keys():
        #     print("{} : {}".format(key, memo[key]))
        
        out = self.xtnMapToOutFormat(memo)
        return out
    
    def xtnMapToOutFormat(self, memo):
        xmin = min(memo.keys())
        xmax = max(memo.keys())
        out = []
        for i in range(xmin, xmax+1):
            vertList = []
            yListsForx = memo[i]
            for yInd in range(len(yListsForx)):
                yList = yListsForx[yInd]
                if yList:
                    if len(yList) == 1:
                        vertList.append(yList[0])
                    else:
                        yListSorted = sorted(yList)
                        vertList += yListSorted
            out.append(vertList)
        return out
    
    def getDepth(self, root):
        if root == None:
            return 0
        
        ld = self.getDepth(root.left)+1
        rd = self.getDepth(root.right)+1
        return max(ld, rd)
    
    def test_getDepth(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        
        d = self.getDepth(root)
        print("d: ", d)
    
    def test1(self):
        arr = [0,8,1,None,None,3,2,None,4,5,None,None,7,6]
        expected = [[8],[0,3,6],[1,4,5],[2,7]]
        
        arr = [0,2,1,3,None,None,None,4,5,None,7,6,None,10,8,11,9]
        # [0,2,1,3,null,null,null,4,5,null,7,6,null,10,8,11,9]

sol = Solution()
sol.test_getDepth()
#sol.test1()