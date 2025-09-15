class BTreeNode():
    def __init__(self, value):
        pass

class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.val = self.value
        self.left = None
        self.right = None

class BinaryTreeUtils:
    @staticmethod
    def printBT(tree):
        h = BinaryTreeUtils.treeHeight(tree)
        for i in range(0,h+1):
            BinaryTreeUtils.printLevel(tree, i)
            print("")

    # https://www.geeksforgeeks.org/print-level-order-traversal-line-line/
    @staticmethod
    def printLevel(tree, treeDepth):
        if tree is None:
            return
        
        if(treeDepth == 1):
            print("{}".format(tree.value), end=' ')
        else:
            BinaryTreeUtils.printLevel(tree.left, treeDepth-1)
            BinaryTreeUtils.printLevel(tree.right, treeDepth-1)
            
    # root is height of 0
    @staticmethod
    def treeHeight(tree):
        if tree is None:
            return 0
        ld = BinaryTreeUtils.treeHeight(tree.left)
        rd = BinaryTreeUtils.treeHeight(tree.right) 
        return max(ld+1, rd+1)

    @staticmethod
    def buildTree(arr): # arr is a tree in array format
        if not arr:
            return None

        def h(arr, i):
            if i > len(arr)-1:
                return None
            if arr[i]==None:
                return None
            
            root = TreeNode(arr[i])
            #print("node created: ", root.val)
            root.left = h(arr, 2*i+1)
            root.right = h(arr, 2*i+2)
            return root
        
        root = h(arr, 0)
        return root

    def test1(self):
        tree = TreeNode(2)
        tree.left = TreeNode(1)
        tree.left.left = TreeNode(0)

        tree.right = TreeNode(5)
        tree.right.left = TreeNode(4)
        tree.right.right= TreeNode(8)
        tree.right.right.left = TreeNode(12)

        d = BinaryTreeUtils.treeHeight(tree)
        print("depth: " + str(d))
        BinaryTreeUtils.printBT(tree)

def main():
    btUtils = BinaryTreeUtils()
    btUtils.test1()

if __name__ == "__main__":
    main()