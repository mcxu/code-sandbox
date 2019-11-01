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

        self.helper(root.left, k, s)

        # evaluation logic, done in-order
        print("root.val={}, s={}".format(root.val, s))
        if s and (k - root.val) in s:
            return True
        else:
            s.add(root.val)

        self.helper(root.right, k, s)

        return False
    
    def test_pairExists(self):
        tree = TreeNode(5)
        tree.left = TreeNode(3)
        tree.left.left = TreeNode(2)
        tree.left.right = TreeNode(4)

        tree.right = TreeNode(6)
        tree.right.right = TreeNode(7)
        
        a = self.pairExists(tree, 9)
        print("a:", a)


    """
    The below implementation reutrns the actual pair instead of
    just True or False.
    """

    def pairExists2(self, root, k):
        return self.helper2(root, k , [])

    # lst: list to store traversed values
    def helper2(self, root, k, lst):
        if root == None:
            return ()

        self.helper2(root.left, k, lst)

        # evaluation logic, done in-order
        print("root.val={}, lst={}".format(root.val, lst))
        
        for ind,val in enumerate(lst):
            if (k-root.val) == val:
                return (root.val, val)

        lst.append(root.val)

        self.helper2(root.right, k, lst)

        return ()
    
    def test_pairExists2(self):
        tree = TreeNode(5)
        tree.left = TreeNode(3)
        tree.left.left = TreeNode(2)
        tree.left.right = TreeNode(4)

        tree.right = TreeNode(6)
        tree.right.right = TreeNode(7)
        
        a = self.pairExists2(tree, 7)
        print("a:", a)



def main():
    lc653 = LC653_TwoSumIv()
    #lc653.test_pairExists()
    lc653.test_pairExists2()

main()




