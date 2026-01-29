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