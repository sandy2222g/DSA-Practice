maze=[
    [0,1,0,0,0]
   ,[0,1,0,0,0] 
   ,[0,0,0,0,0] 
   ,[0,1,1,0,1] 
   ,[1,0,1,0,0] 
   ,[1,0,1,0,0] 
   ,[1,0,1,0,0] 
   ,[1,0,1,0,0] 
   ,[1,0,1,0,0] 
   ,[1,0,1,0,0] 
   ,[1,0,1,0,0] 
]
m=5
n=11
dp=[[float('inf')]*(m+1) for i in range(n+1)]
dp[1][1]=0
for i in range(1,n+1):
    for j in range(1,m+1):
        if maze[i-1][j-1]==1 or dp[i][j]==0:
            continue
        dp[i][j]=min(dp[i-1][j],dp[i][j-1])+1

for i in dp:
    print(i)

print(dp[11][5])

print(min([[1,2,3],[1,2],[1]]))