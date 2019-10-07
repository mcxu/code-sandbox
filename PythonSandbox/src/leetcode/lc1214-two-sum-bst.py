"""
1214. Two Sum BSTs [Medium]
Given two binary search trees, return True if and only if there is a 
node in the first tree and a node in the second tree whose values 
sum up to a given integer target.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    

class LC1214_TwoSumBSTs:
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        if root1==None:
            return False
        if root2==None:
            return False
        print("root1val:{}, root2val:{}".format(root1.val, root2.val))
        sum = root1.val + root2.val
        print(" sum: {}, target: {}".format(sum,target))
        if(sum == target):
            return True
        
        if sum < target:
            if root1.val < root2.val:
                print(" sum<target, sel r1 right")
                if root1.right != None:
                    return self.twoSumBSTs(root1.right, root2, target)
            else: #root1.val > root2.val:
                print(" sum<target, sel r2 right")
                if root2.right != None:
                    return self.twoSumBSTs(root1, root2.right, target)
        elif sum > target:
            if root1.val < root2.val:
                print(" sum>target, sel r2 left")
                if root2.left != None:
                    return self.twoSumBSTs(root1, root2.left, target)
            else: #root1.val > root2.val:
                print(" sum>target, sel r1 left")
                if root1.left != None:
                    return self.twoSumBSTs(root1.left, root2, target)
        else:
            print("else")
            return False


    def test1_twoSumBSTs(self):
        tree = TreeNode(2)
        tree.left = TreeNode(1)
        tree.left.left = TreeNode(0)
        #tree.right = TreeNode(4)
        d = self.treeDepth(tree)
        print("depth: " + str(d))
        #self.printBT(tree)


    def printBT(self, tree):
        self.printHelper(tree, self.treeDepth(tree))
    
    def printHelper(self, tree, treeDepth):
        #TODO fix
        if tree == None:
            return
        s = "{}".format(tree.val)
        print(s)
        if tree.left is not None:
            self.printBT(tree.left)
        if tree.right is not None:
            self.printBT(tree.right)
    
    # root is depth of 0
    def treeDepth(self, tree):
        if tree is None:
            return 0
        if tree.left or tree.right is not None:
            ld = self.treeDepth(tree.left)
            rd = self.treeDepth(tree.right)
            if rd > ld:
                return rd+1
            else:
                return ld+1
        else:
            return 0


def main():
    lc1214 = LC1214_TwoSumBSTs()
    lc1214.test1_twoSumBSTs()

main()