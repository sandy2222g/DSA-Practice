# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        r=[]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            r.append(root.val)
            dfs(root.right)
        dfs(root)
        
        def tree(l,rr):
            if l> rr:
                return None
            m=(l+rr)//2
            root=TreeNode(r[m])
            root.left=tree(l,m-1)
            root.right=tree(m+1,rr)

            return root
        
        return tree(0,len(r)-1)
            