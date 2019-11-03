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
    """
    :type root: TreeNode
    :type k: int
    :rtype: bool
    """
    def pairExists(self, root, k):
        s = set()
        return self.helper(root, k, s)
    
    # s is a set()
    def helper(self, root, k, s):
        if root == None:
            return False

        if self.helper(root.left, k, s):
            return True

        # evaluation logic, done in-order
        print("root.val={}, s={}".format(root.val, s))
        if s and (k - root.val) in s:
            print("    d={}, s={}".format(k-root.val, s))
            return True
        else:
            s.add(root.val)

        return self.helper(root.right, k, s)
    
    
    def test_pairExists(self):
        tree = TreeNode(5)
        tree.left = TreeNode(3)
        tree.left.left = TreeNode(2)
        tree.left.right = TreeNode(4)

        tree.right = TreeNode(8)
        tree.right.left = TreeNode(6)
        tree.right.right = TreeNode(9)
        
        a = self.pairExists(tree, 13)
        print("a:", a)

    def test_pairExists2(self):
        tree = TreeNode(5)
        tree.left = TreeNode(3)
        tree.left.left = TreeNode(2)
        tree.left.right = TreeNode(4)
        
        tree.right = TreeNode(6)
        tree.right.right = TreeNode(7)
        
        a = self.pairExists(tree, 14)
        print("a:", a)
        


    """
    The below implementation reutrns the actual pair instead of
    just True or False.
    """

    def getBSTPair(self, root, k):
        return self.helper2(root, k , set())

    # lst: list to store traversed values
    def helper2(self, root, k, s):
        if root == None:
            return ()

        if self.helper2(root.left, k, s):
            return (k-root.val, root.val)

        # evaluation logic, done in-order
        print("root.val={}, s={}".format(root.val, s))
        if s and (k-root.val) in s:
            return (k-root.val, root.val)
        else:
            s.add(root.val)

        return self.helper2(root.right, k, s)
    
    def test_getBSTPair(self):
        tree = TreeNode(5)
        tree.left = TreeNode(3)
        tree.left.left = TreeNode(2)
        tree.left.right = TreeNode(4)

        tree.right = TreeNode(8)
        tree.right.left = TreeNode(6)
        tree.right.right = TreeNode(9)
        
        a = self.getBSTPair(tree, 14)
        print("a:", a)

    def test_getBSTPair2(self):
        tree = TreeNode(5)
        tree.left = TreeNode(3)
        tree.left.left = TreeNode(2)
        tree.left.right = TreeNode(4)
        
        tree.right = TreeNode(6)
        tree.right.right = TreeNode(7)
        
        a = self.pairExists(tree, 5)
        print("a:", a)


def main():
    lc653 = LC653_TwoSumIv()
    #lc653.test_pairExists()
    #lc653.test_pairExists2()
    #lc653.test_getBSTPair()
    lc653.test_getBSTPair2()

main()




