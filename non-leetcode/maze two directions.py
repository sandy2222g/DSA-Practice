n=int(input())
r=[list(map(int,input().split())) for _ in range(n)]        
sol=[[0]*n for _ in range(n)]
def bt(x,y):
    if x>=n or y>=n or r[x][y]==1:
        return 
    if x==n-1 and y==n-1:
        sol[x][y]=1
        for i in sol:
            print(*i)
        exit()
    sol[x][y]=1
    bt(x+1,y)
    bt(x,y+1)
    sol[x][y]=0
bt(0,0)
print("No solution exists")