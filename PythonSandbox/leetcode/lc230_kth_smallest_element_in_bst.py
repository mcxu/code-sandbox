'''
230. Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Note: You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int: 
        #using inorder traversal on a BST can get sorted array of values
        def helper(root, values):
            if root == None:
                return
            
            helper(root.left,values)
            values.append(root.val)
            helper(root.right,values)
            
        values=[]
        helper(root, values)
        return values[k-1]
    
    def test1(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        k=1
        res = self.kthSmallest(root, k)
        print("test1 res: ", res)
    
    def test2(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)
        root.left.left = TreeNode(2)
        root.left.right= TreeNode(4)
        root.left.left.left = TreeNode(1)
        k = 3
        res = self.kthSmallest(root, k)
        print("test2 res: ", res)

# sol = Solution()
#sol.test1()
# sol.test2()

# Solution 2: Using heap
class Solution2:
    def kthSmallest(self, root: [], k: int) -> int:
        heapArr = []
        self.putOnHeap(root, heapArr)

        kthSmallest = -float('inf')
        for i in range(k):
            kthSmallest = heapq.heappop(heapArr)
        
        return kthSmallest

    def putOnHeap(self, root, heapArr):
        if root == None:
            return
        
        heapq.heappush(heapArr, root.val)

        self.putOnHeap(root.left, heapArr)
        self.putOnHeap(root.right, heapArr)


# Solution 3: Using inorder traversal, but stops at kth recursion
class Solution3:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodeValues = []
        self.inorderTraverse(root, nodeValues, k)
        return nodeValues[-1]

    def inorderTraverse(self, root, nodeValues, k):
        if root == None:
            return 
        
        self.inorderTraverse(root.left, nodeValues, k)
        if len(nodeValues) >= k:
            return
        else:
            nodeValues.append(root.val)
        self.inorderTraverse(root.right, nodeValues, k)
