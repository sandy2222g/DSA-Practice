class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        m=-float("inf")
        def dfs(root):
            nonlocal m
            if not root:
                return 0
            
            l=max(0,dfs(root.left))
            r=max(0,dfs(root.right))

            m=max(m,l+r+root.val)
            return max(l,r)+root.val
        dfs(root)
        return m