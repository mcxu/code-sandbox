class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return 0

        deepestValidDepthSoFar = 0
        validNode = root

        # iterative dfs
        stack = [(root, 0)] # (node, depth)
        while stack:
            currItem = stack.pop(-1)
            currNode, currDepth = currItem[0], currItem[1]
            # print("==== Outer DFS from currNode: ", currNode.val if currNode != None else None)
            if currNode != None:
                seenValues = set()
                # print("Running inner dfs on currNode: ", currNode.val)
                self.verifyPandQExistFromRoot(currNode, p, q, seenValues)
                # print("seenValues: after: ", seenValues)
                pqExistsFromRoot = (p.val in seenValues) and (q.val in seenValues)
                # print("pqExistsFromRoot: ", pqExistsFromRoot)
                if pqExistsFromRoot and currDepth > deepestValidDepthSoFar:
                    deepestValidDepthSoFar = currDepth
                    validNode = currNode
                
                stack.append((currNode.right, currDepth+1))
                stack.append((currNode.left, currDepth+1))

        return validNode

    def verifyPandQExistFromRoot(self, root, p, q, seenValues):
        if root == None:
            return 

        if p.val in seenValues and q.val in seenValues:
            return 
        
        seenValues.add(root.val)

        self.verifyPandQExistFromRoot(root.left, p, q, seenValues)
        self.verifyPandQExistFromRoot(root.right, p, q, seenValues)