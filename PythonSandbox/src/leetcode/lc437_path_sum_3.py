'''
437. You are given a binary tree in which each node contains an integer value.
Find the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:
1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.count = 0
    
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.traverse(root, sum)
        return self.count
    
    def traverse(self, root, sum):
        if root == None:
            return
        #print("traverse: val: {}, count: {}".format(root.val, self.count))
        self.getCounts(root,sum, 0)
        #print("traverse: count after getCounts: ", self.count)
        self.traverse(root.left, sum)
        self.traverse(root.right, sum)
    
    # get number of paths that add up to sum from a given root
    def getCounts(self, root, sum, runSum):
        if root == None:
            return 
        #print(" root: ", root.val)
        runSum += root.val
        #print(" runSum: ", runSum)
        if runSum == sum:
            self.count += 1
            #print(" updating count: ", self.count)
        
        self.getCounts(root.left, sum, runSum)
        self.getCounts(root.right, sum, runSum)
    
    def tree1(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.left.right = TreeNode(-2)
        root.left.right = TreeNode(2)
        root.left.right.right = TreeNode(1)
        root.right = TreeNode(-3)
        root.right.right = TreeNode(11)
        return root
    
    def test1(self):
        root = self.tree1()
        sum = 8
        self.count = 0
        self.pathSum(root, sum)
        print("test1: count: ", self.count)
        
# sol = Solution()
# sol.test1()

class Solution2:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root == None:
            return 0
        countFromRoot = self.getCounts(root, sum)
        print("root.val: {}, countFromRoot: {}".format(root.val, countFromRoot))
        countFromLeft = self.pathSum(root.left, sum)
        countFromRight = self.pathSum(root.right, sum)
        return countFromRoot + countFromLeft + countFromRight
    
    # get number of paths that add up to sum from a given root
    def getCounts(self, root, sum, runSum=0):
        if root == None:
            return 0
        print("root: {}, sum: {}, runSum: {}".format(root.val,sum,runSum))
        runSum += root.val
        countIncludingRoot = 0
        if runSum == sum:
            countIncludingRoot = 1
        lc = self.getCounts(root.left, sum, runSum)
        print("    lc: ", lc)
        rc = self.getCounts(root.right, sum, runSum)
        print("    rc: ", rc)
        print("returning: ", lc+rc)
        return countIncludingRoot + lc + rc
    
    def tree1(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.left.right = TreeNode(-2)
        root.left.right = TreeNode(2)
        root.left.right.right = TreeNode(1)
        root.right = TreeNode(-3)
        root.right.right = TreeNode(11)
        return root
    
    def tree2(self):
        root = TreeNode(1)
        root.left = TreeNode(-2)
        root.left.left = TreeNode(1)
        root.left.left.left = TreeNode(-1)
        root.right = TreeNode(-3)
        root.right.left = TreeNode(-2)
        return root
    
    def test1(self):
        root = self.tree1()
        counts = self.getCounts(root.right, 8)
        print("test1: counts: ", counts)
    
    def test2(self):
        root = self.tree1()
        counts = self.pathSum(root, 8)
        print("test2: counts: ", counts)
        
    def test3(self):
        root = self.tree2()
        counts = self.pathSum(root, -1)
        print("test3: counts: ", counts)
        
sol2 = Solution2()
#sol2.test1()
#sol2.test2()
#sol2.test3()

''' Reference:
https://medium.com/@lenchen/leetcode-437-path-sum-iii-c5c1f6bf7d67
'''