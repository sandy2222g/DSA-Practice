arr=eval(input())
n=int(input())
dp=[[[],i] for i in range(n+1)]
for i in range(0,n):
    if not(dp[i][0]) and i!=0:
        continue
    for j in arr:
        for k in dp[i][0]:
            if i+j<n+1:
                dp[i+j][0].append(k+[j])
        if dp[i][0]==[]:
            dp[i+j][0].append([j])

print(min(dp[n][0]))
