"""
Function that takes BT and returns a list of its branch sums, from left to right branch.
Branch sum: sum of all values in a binary tree branch.
Binary tree branch: path of nodes in tree that starts at root node and ends at any leaf node.

Sample input:
          1
        /   \
       2     3
      / \   / \ 
     4   5 6   7
    / \   \
   8   9   10
Sample output: [15,16,18,10,11]
"""
class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Prob:
    """
    Use depth first search since getting paths involve traversing deeper into tree.
    """
    @staticmethod
    def branchSums(root):
        sums = []
        Prob.dfs(root, 0, sums)
        return sums
    
    @staticmethod
    def dfs(root, runSum=0, sums=[]):
        if root == None:
            return root
        
        print("value: ", root.value)
        runSum += root.value
        if root.left is None and root.right is None:
            sums.append(runSum)
        print("    sums: ", sums)
            
        Prob.dfs(root.left, runSum, sums)
        Prob.dfs(root.right, runSum, sums)
    
    
    @staticmethod
    def tree1():
        tree = BTNode(1)
        tree.left = BTNode(2)
        tree.left.left = BTNode(4)
        tree.left.right = BTNode(5)
        tree.left.right.right = BTNode(10)
        tree.left.left.left = BTNode(8)
        tree.left.left.right = BTNode(9)
        tree.right = BTNode(3)
        tree.right.left = BTNode(6)
        tree.right.right = BTNode(7)
        return tree
    
    @staticmethod
    def test_dfs():
        sums=[]
        Prob.dfs(Prob.tree1(), 0, sums)
        print("sums:", sums)
    
    @staticmethod
    def test_branchSums():
        sums = Prob.branchSums(Prob.tree1())
        print("sums: ", sums)

#Prob.test_dfs()
Prob.test_branchSums()
