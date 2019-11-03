"""
1214. Two Sum BSTs [Medium]
Given two binary search trees, return True if and only if there is a 
node in the first tree and a node in the second tree whose values 
sum up to a given integer target.
"""

from utils.binary_tree_utils import TreeNode
from utils.binary_tree_utils import BinaryTreeUtils as BTUtils

class LC1214_TwoSumBSTs:
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """  
        s = set()
        self.helper1(root1, s)
        print("twoSumBSTs: s: ", s)
        result = self.helper2(root2, target, s)
        print("twoSumBSTs: result: ", result)
        return result
    
    # do in-order traversal on 1st BST so that the elements in the tree
    # are put on the list in sorted order.
    def helper1(self, root, s):
        if root == None:
            return
        self.helper1(root.left, s)
        print("helper1: val:", root.val)
        s.add(root.val)
        self.helper1(root.right, s)
    
    # do in-order traversal on 2nd BST, while comparing each element
    # from the 2nd tree to the ones on l1 (from the 1st tree)
    def helper2(self, root, target, s):
        if root == None:
            return False
        
        if self.helper2(root.left, target, s):
            return True
        
        # evaluation logic
        print("helper2: val: {}, target: {}".format(root.val, target))
        d = target - root.val # difference that needs to be found in l1
        if d > 0 and d in s:
            print("    d={}, s={}".format(d, s))
            return True
        
        return self.helper2(root.right, target, s)
        

    def tree1(self):
        tree = TreeNode(2)
        tree.left = TreeNode(1)
        tree.left.left = TreeNode(0)
        tree.right = TreeNode(5)
        tree.right.left = TreeNode(4)
        tree.right.right = TreeNode(6)
#         d = BTUtils.treeHeight(tree)
#         print("depth: " + str(d))
#         BTUtils.printBT(tree)
        return tree
    
    def tree2(self):
        tree = TreeNode(2)
        tree.left = TreeNode(1)
        tree.right = TreeNode(3)
        tree.right.right = TreeNode(4)
        return tree
    
    def tree3(self):
        tree = TreeNode(5)
        tree.left = TreeNode(4)
        tree.left.left = TreeNode(3)
        tree.right = TreeNode(7)
        return tree

    def test1(self):
        a = self.twoSumBSTs(self.tree2(), self.tree3(), 5)
        print("test1: ans: ", a)
    
    def test2(self):
        a = self.twoSumBSTs(self.tree1(), self.tree3(), 12)
        print("test1: ans: ", a)

def main():
    lc1214 = LC1214_TwoSumBSTs()
    
    BTUtils.printBT(lc1214.tree1())
    
    #lc1214.test1()
    lc1214.test2()

main()
