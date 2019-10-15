"""
653. Two Sum IV - Input is a BST [Easy]
Given a Binary Search Tree and a target number, return true if there exist 
two elements in the BST such that their sum is equal to the given target.
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class LC653_TwoSumIv:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root is None:
            return true

    def test_findTarget(self):
        tree = TreeNode(5)
        tree.left = TreeNode(3)
        tree.left.left = TreeNode(2)
        tree.left.right = TreeNode(4)

        tree.right = TreeNode(6)
        tree.right.right = TreeNode(7)
        
        target = 9


def main():
    lc653 = LC653_TwoSumIv()
    lc653.test_findTarget()

main()




