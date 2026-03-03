'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = [None]
        self.dfs(root, p, q, ancestor)
        return ancestor[0]
    
    def dfs(self, root, p, q, ancestor):
        if root == None:
            return False
            
        leftContainsVal = self.dfs(root.left, p, q, ancestor)
        rightContainsVal= self.dfs(root.right, p, q, ancestor)
        
        atLeast1Match = False
        if root.val==p.val or root.val==q.val:
            atLeast1Match = True
            
        if leftContainsVal + rightContainsVal + atLeast1Match >= 2:
            ancestor[0] = root
        
        return leftContainsVal or rightContainsVal or atLeast1Match

# Results in TLE (O(n^2) time solution)
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         parent = None
#         soln = []
#         self.helper(root, p, q, parent, soln)
#         print("soln: ", soln)
#         if not soln:
#             return None
#         return soln[0]
    
#     def helper(self, root, p, q, parent, soln):
#         if root == None:
#             return 
#         #print("helper root: {}, p:{}, q:{}, parent:{}".format(root.val, p.val, q.val, parent.val if parent else None))
#         targets = []
#         self.dfs(root, p, q, targets)
#         #print("targets: ", targets)
        
#         if (root.val==p.val or root.val==q.val) and (p.val in targets and q.val in targets):
#             soln.append(root)
#             return
#         elif p.val in targets and q.val not in targets:
#             soln.append(parent)
#             return 
#         elif p.val not in targets and q.val in targets:
#             soln.append(parent)
#             return 
            
#         self.helper(root.left, p, q, root, soln)
#         self.helper(root.right, p, q, root, soln)
    
#     def dfs(self, root, p, q, targets):
#         if root == None:
#             return
#         if p and root.val==p.val:
#             targets.append(p.val)
#         elif q and root.val==q.val:
#             targets.append(q.val)
#         self.dfs(root.left, p, q, targets)
#         self.dfs(root.right, p, q, targets)