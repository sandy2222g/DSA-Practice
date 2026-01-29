"""
  **using Memoization **


from functools import lru_cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])

        @lru_cache(None)
        def dfs(i,j):
            if i<0 or j<0:
                return float('inf')
            if i==j==0:
                return grid[0][0]
            return grid[i][j]+min(
                dfs(i-1,j),dfs(i,j-1)
            )
        return dfs(n-1,m-1)


        
        **Tabulation (2D DP array)**


        class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[float('inf')]*m for _ in range(n)]
        dp[0][0]=grid[0][0]
        for i in range(1,n):
            dp[i][0]=dp[i-1][0] + grid[i][0]
        for i in range(1,m):
            dp[0][i]=dp[0][i-1]+grid[0][i]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return(dp[n-1][m-1])
        
        
        
        
        
        
        **Tabulation (1D DP array)**

        class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[float('inf')]*m
        dp[0]=0
        for i in range(n):
            for j in range(m):
                if j==0:
                    dp[j]=dp[j]+grid[i][j]
                else:
                    dp[j]=min(dp[j],dp[j-1])+grid[i][j]
        return dp[m-1] 
        
        
        
        
        """