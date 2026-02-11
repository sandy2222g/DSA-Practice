def sol(arr):
    n=len(arr)
    dp=[0]*(n+1)
    for i in range(1,n+1):
        dp[i]=max(arr[i-1],dp[i-1]+arr[i-1])
    return max(dp)
print(sol([-2,1,-3,4,-1,2,1,-5,4]))