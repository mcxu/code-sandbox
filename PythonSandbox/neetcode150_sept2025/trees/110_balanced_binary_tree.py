from utils.binary_tree_utils import TreeNode, BinaryTreeUtils as BTU

class BalancedBT:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        diff = abs(rightHeight - leftHeight)

        if diff > 1:
            return False
        
        subtreeIsBalanced = self.isBalanced(root.left) and self.isBalanced(root.right)
        return subtreeIsBalanced

    
    def getHeight(self, root):
        if not root:
            return 0
        
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        return 1 + max(leftHeight, rightHeight)

    def test1(self):
        root = [1,2,2,3,None,None,3,4,None,None,4]
        rootNode = BTU.buildTree(root)
        result = self.isBalanced(rootNode)
        print("result: ", result)

if __name__ == "__main__":
    c = BalancedBT()
    c.test1()