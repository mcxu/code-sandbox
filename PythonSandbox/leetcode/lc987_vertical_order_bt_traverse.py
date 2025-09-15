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
    def verticalTraversal(self, root: TreeNode) -> [[int]]:
        colMap = {}
        x = 0
        y = 0
        self.helper(root, colMap, x, y)
        out=[]
        for k in sorted(colMap.keys()):
            tupList = sorted(colMap[k], key=lambda x: x[1])
            yMap = {}
            for _,t in enumerate(tupList):
                rv = t[0]; yv = t[1]
                if yv in yMap.keys():
                    yMap[yv].append(rv)
                else:
                    yMap[yv] = [rv]
            #print("yMap: ",yMap)
            col = []
            for k in sorted(yMap.keys()):
                col += sorted(yMap[k])
            out.append(col)
        return out
    
    def helper(self, root, colMap, x, y):
        if root == None:
            return
        
        if x in colMap.keys():
            colMap[x].append((root.val,y))
        else:
            colMap[x] = [(root.val,y)]
        #print("colMap: ", colMap)
        self.helper(root.left, colMap, x-1, y+1)
        self.helper(root.right, colMap, x+1, y+1)
    
    def buildTree(self, arr):
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

    def test1(self):
        arr = [3,9,20,None,None,15,7]
        expected = [[9],[3,15],[20],[7]]
        root = self.buildTree(arr)
        res = self.verticalTraversal(root)
        print("res: ", res)

    def test2(self):
        arr = [1,2,3,4,5,6,7]
        expected = [[4],[2],[1,5,6],[3],[7]]
        root = self.buildTree(arr)
        res = self.verticalTraversal(root)
        print("res: ", res)
        if res==expected:
            print("test2 pass")

    def test3(self):
        arr = [0,2,1,3,None,None,None,4,5,None,7,6,None,10,8,11,9]
        expected = [[4,10,11],[3,6,7],[2,5,8,9],[0],[1]]
        root = self.buildTree(arr)
        res = self.verticalTraversal(root)
        print("res: ", res)
        if res==expected:
            print("test3 pass")

sol = Solution()
#sol.test1()
#sol.test2()
sol.test3()