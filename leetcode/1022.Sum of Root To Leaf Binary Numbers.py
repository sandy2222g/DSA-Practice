class Solution:
    def sumRootToLeaf(self, root):
        def dfs(node=root, current=0):
            if not node:
                return 0
            current=current*2+node.val  
            if not node.left and not node.right:
                return current        
            return dfs(node.left,current)+dfs(node.right,current)
        return dfs()