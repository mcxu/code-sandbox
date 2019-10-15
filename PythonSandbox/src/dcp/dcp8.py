"""
This problem was asked by Google. [Easy]

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

 0
/ \
1   0
    / \
    1   0
    / \
    1   1
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class DCP8():
    def countUnivalSubtrees(self, root):
        if root == None:
            return 0
        else:
            thisTreeUnival = self.isTreeUnival(root)
            print("countUnivalSubtrees: thisTreeUnival:", thisTreeUnival)
            numLeftTrees = self.countUnivalSubtrees(root.left)
            print("countUnivalSubtrees: numLeftTrees: {} at rootval: {}".format(numLeftTrees, root.val))
            numRightTrees = self.countUnivalSubtrees(root.right)
            print("countUnivalSubtrees: numRightTrees: {} at rootval: {}".format(numRightTrees, root.val))
            
            if thisTreeUnival:
                return 1 + numLeftTrees + numRightTrees
            else:
                return numLeftTrees + numRightTrees
            

    # determine if tree is a unival tree from a given node downwards to leaves
    def isTreeUnival(self, node):
        if node.left != None and node.right != None:
            print("A")
            if node.left.val == node.val and node.right.val == node.val:
                print("B")
                return (self.isTreeUnival(node.left) and self.isTreeUnival(node.right))
            else:
                print("G")
                return False
        elif node.left != None:
            print("C")
            if node.left.val == node.val:
                print("D")
                return self.isTreeUnival(node.left)
            else:
                print("I")
                return False
        elif node.right != None:
            print("E")
            if node.right.val == node.val:
                print("F")
                return self.isTreeUnival(node.right)
            else:
                print("L")
                return False
        else:
            print("K")
            return True
    

    # given in problem
    def testTree1(self):
        tree = TreeNode(0)
        tree.left = TreeNode(1)
        tree.right = TreeNode(0)
        tree.right.left = TreeNode(1)
        tree.right.right = TreeNode(0)
        tree.right.left.left = TreeNode(1)
        tree.right.left.right = TreeNode(1)
        return tree

    def testTree2(self):
        tree = TreeNode(0)
        tree.left = TreeNode(1)
        tree.right = TreeNode(0)
        return tree
    
    def testTree3(self):
        tree = TreeNode(0)
        tree.left = TreeNode(1)
        # tree.right = TreeNode(1)
        # tree.right.right = TreeNode(0)
        return tree


    def test_isTreeUnival(self):
        tree = self.testTree1()
        result = self.isTreeUnival(tree.right.right)
        print("result: {}".format(result))
    
    def test_countUnivalSubtrees(self):
        tree = self.testTree1()
        ct = self.countUnivalSubtrees(tree)
        print("test_countUnivalSubtrees: count: {}".format(ct))

def main():
    dcp8 = DCP8()
    
    #dcp8.test_isTreeUnival()
    dcp8.test_countUnivalSubtrees()

        
if __name__ == "__main__":
    main()