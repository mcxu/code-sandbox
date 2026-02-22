from utils.binary_tree_utils import TreeNode, BinaryTreeUtils as BTU

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        mpsSoFar = [-float('inf')]
        _ = self.gainFromNode(root, mpsSoFar)
        return mpsSoFar[0]
    
    def gainFromNode(self, root, mpsSoFar):
        if not root:
            return 0
        
        leftGain = max(0, self.gainFromNode(root.left, mpsSoFar))
        rightGain = max(0, self.gainFromNode(root.right, mpsSoFar))

        # calculate the max path sum seen so far
        gainFromBothSides = root.val + leftGain + rightGain
        mpsSoFar[0] = max(mpsSoFar[0], gainFromBothSides)

        # calculate the gain from one side, bc the recursive calls for the children need it
        gainFromMaxSide = max(leftGain, rightGain) + root.val # including root value
        print("recursion: mpsSoFar: ", mpsSoFar, "    gainFromMaxSide: ", gainFromMaxSide)
        return gainFromMaxSide


    def test1(self):
        treeArr = [-10,9,20,None,None,15,7]
        tree = BTU.buildTree(treeArr)
        mps = self.maxPathSum(tree)
        print("mps: final: ", mps)
    
    def test2(self):
        treeArr = [-3]
        tree = BTU.buildTree(treeArr)
        mps = self.maxPathSum(tree)
        print("mps: final: ", mps)

if __name__ == "__main__":
    c = Solution()
    #c.test1()
    c.test2()