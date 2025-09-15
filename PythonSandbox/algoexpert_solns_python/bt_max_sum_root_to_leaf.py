'''
Given binary tree, get the max root to leaf sum,
as well as the corresponding path. If the max sum has more than 1 path,
then return all paths.
Ref: https://www.geeksforgeeks.org/find-the-maximum-sum-path-in-a-binary-tree/

Example:
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return: [27, [[5, 4, 11, 7]]]
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Prob:
    '''
    Let n = number of nodes in tree.
    Time complexity: O(n): O(n) from root helper call, O(n) for finding max key in pathMap.
    Space complexity: O(n): from using the helper.
    '''
    @staticmethod
    def maxSumPath(root):
        pathMap = {} # store: pathSum:[list of values corresponding to path]
        Prob.helper(root, 0, [], pathMap) # O(n) time
        maxSum = max(pathMap.keys()) # O(n) time
        maxSumPath = pathMap[maxSum]
        return [maxSum, maxSumPath]

    '''
    Let n = number of nodes in tree.
    Time complexity: O(n), since recursion goes through all nodes.
    Space complexity: O(n), n helper calls in recursion stack, 
        and pathMap stores at most n items for some path sum. -> 2*n
    '''
    @staticmethod
    def helper(root, runSum, path, pathMap):
        if root == None:
            return
        runSum += root.val
        if root.left==None and root.right==None:
            pathCopy = path.copy()
            pathCopy.append(root.val)
            if runSum not in pathMap.keys():
                pathMap[runSum] = [pathCopy]
            else:
                pathMap[runSum].append(pathCopy)
        
        Prob.helper(root.left, runSum, path+[root.val], pathMap)
        Prob.helper(root.right, runSum, path+[root.val], pathMap)

    @staticmethod
    def test1():
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right = TreeNode(8)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.left = TreeNode(5)
        root.right.right.right = TreeNode(1)
        
        res = Prob.maxSumPath(root)
        print("test1 res: ", res)

Prob.test1()