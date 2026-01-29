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