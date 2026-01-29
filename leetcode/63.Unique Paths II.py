class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        dp=[[0]*(m+1) for _ in range(n+1)]
        dp[1][1]=1
        for i in range(1,n+1):
            for j in range(1,m+1):
                if i==j==1 or obstacleGrid[i-1][j-1]==1:
                    continue
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

obj=Solution()
print(obj.uniquePathsWithObstacles([[0,0,0,0],[0,0,1,0],[0,0,0,0],[1,0,0,0]]))


"""

    **memoization**

from functools import lru_cache
class Solution:
    def uniquePathsWithObstacles(self, ob: List[List[int]]) -> int:
        if ob[0][0]==1:
            return 0
        n=len(ob)
        m=len(ob[0])
        @lru_cache(None)
        def dfs(i,j):
            if i<0 or j<0 or ob[i][j]==1:
                return 0
            if j==i==0:
                return 1
            return dfs(i-1,j)+dfs(i,j-1)
        return dfs(n-1,m-1)

"""