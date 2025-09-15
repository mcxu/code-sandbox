'''
https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic 
if at least one permutation of the node values in the path is a palindrome.
Return the number of pseudo-palindromic paths going from the root node to leaf nodes.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#test case to use:
#[9,5,4,5,null,2,6,2,5,null,8,3,9,2,3,1,1,null,4,5,4,2,2,6,4,null,null,1,7,null,5,4,7,null,null,7,null,1,5,6,1,null,null,null,null,9,2,null,9,7,2,1,null,null,null,6,null,null,null,null,null,null,null,null,null,5,null,null,3,null,null,null,8,null,1,null,null,8,null,null,null,null,2,null,8,7]

class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        currPath = set([root.val])
        validPathCount = []
        self.dfs(root, currPath, validPathCount)
        #print("validPathCount after: ", validPathCount)
        if validPathCount: 
            return validPathCount[0]
        return 0

    def dfs(self, root, currPath, validPathCount):
        if root == None:
            return
        #print("root: ", root.val)
        #print("currPath: ", currPath)
        if not root.left and not root.right:
            if len(currPath) == 1 or len(currPath) == 0:
                if not validPathCount:
                    validPathCount.append(1)
                else:
                    validPathCount[0] += 1
            #print("validPathCount!!!: ", validPathCount)
            return

        if root.left:
            cc = currPath.copy()
            if root.left.val not in cc:
                cc.add(root.left.val)
            else:
                cc.remove(root.left.val)
            self.dfs(root.left, cc, validPathCount)
        if root.right:
            cc = currPath.copy()
            if root.right.val not in cc:
                cc.add(root.right.val)
            else:
                cc.remove(root.right.val)
            self.dfs(root.right, cc, validPathCount)

    #==========================================================================

    # This results in TLE
    def pseudoPalindromicPaths2(self, root: TreeNode) -> int:
        if root == None:
            return None
        
        currPath = [root.val]
        allPaths = []
        self.getAllPaths(root, currPath, allPaths)
        #print("allPaths: ", allPaths)
        
        #test = [1,2,3]
        # self.permuteArray(test, permutations)
        # print("permutations: ", permutations)
        pseudos = 0
        for i,path in enumerate(allPaths):
            permutations = []
            palPerms = []
            self.permuteArray(path, permutations, palPerms)
            #print("palPerms: ", palPerms)
            if palPerms:
                pseudos += 1
        return pseudos

    def isPal(self,arr):
        for i in range(int(len(arr)/2)):
            if arr[i] != arr[-1-i]:
                return False
        return True
    
    def permuteArray(self, arr, permutations, palPerms):
        if arr in permutations:
            return
        else:
            arrCopy = arr.copy()
            permutations.append(arrCopy)
            if self.isPal(arrCopy):
                palPerms.append(arrCopy)
                return
        
        for i in range(len(arr)-1):
            arr[i],arr[i+1]=arr[i+1],arr[i]
            self.permuteArray(arr, permutations, palPerms)
            arr[i],arr[i+1]=arr[i+1],arr[i]
        
    def getAllPaths(self, root, currPath, allPaths):
        if root == None:
            return
        
        if not root.left and not root.right:
            if currPath not in allPaths:
                allPaths.append(currPath)
        
        if root.left:
            self.getAllPaths(root.left, currPath+[root.left.val], allPaths)
        
        if root.right:
            self.getAllPaths(root.right, currPath+[root.right.val], allPaths)
    
    # ======================================================

    def test1(self, alg):
        root = TreeNode(2)
        root.left = TreeNode(3)
        root.right = TreeNode(1)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(1)
        root.right.right = TreeNode(1)

        res = self.pseudoPalindromicPaths(root)
        print("test1 res: ", res)

sol = Solution()
alg = sol.pseudoPalindromicPaths
sol.test1(alg)