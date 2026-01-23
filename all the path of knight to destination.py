n=5
dest=[4,4]
solution=[[0]*n for _ in range(n)]
m=float('inf')
path=0
def knights_tour(x,y,count=0):
    if [x,y]==dest:
        solution[x][y]=1
        global m
        m=min(m,count)
        print(solution)
        path+=1
        return False
    if count>m:
        return False
    if 0 <= x < n and 0 <= y < n and solution[x][y]==0:
        solution[x][y] = 1
        if knights_tour(x+1,y+2,count+1):
            return True
        if knights_tour(x+1,y-2,count+1):
            return True
        if knights_tour(x-1,y+2,count+1):
            return True
        if knights_tour(x-1,y-2,count+1):
            return True
        if knights_tour(x+2,y+1,count+1):
            return True
        if knights_tour(x+2,y-1,count+1):
            return True
        if knights_tour(x-2,y+1,count+1):
            return True
        if knights_tour(x-2,y-1,count+1):
            return True
        solution[x][y] = 0
    return False

knights_tour(0,0)

print(m,path)