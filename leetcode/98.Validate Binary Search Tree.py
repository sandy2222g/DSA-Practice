class Solution:
    def isValidBST(self, root: Optional[TreeNode],l=None) -> bool:
        def rr(root,m=float('inf'),mi=-float("inf")):
            if not root:
                return True
            if root.val<=mi or root.val>=m:
                return False
            
            return rr(root.left,m=root.val,mi=mi) and rr(root.right,m=m,mi=root.val) 
        return rr(root)