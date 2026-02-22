from utils.binary_tree_utils import TreeNode, BinaryTreeUtils as BTU

"""
Time complexity: O(n), n nodes in tree
Space complexity: O(n), O(n) for recursion stack, O(n) for elements, O(2n) still O(n)
"""

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        elements = []
        self.inorder(root, k, elements)
        return elements[-1]

    def inorder(self, root, k, elements):
        if not root:
            return 
        
        self.inorder(root.left, k, elements)

        if len(elements) == k:
            return
        else:
            elements.append(root.val)

        self.inorder(root.right, k, elements)


