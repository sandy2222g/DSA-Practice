"""

**single solution**


n=4
sol=[['.']*n for _ in range(n)]
col=set()
d1=set()
d2=set()

def backtrack(r):
    if r==n:
        for i in range(n):
            print("".join(sol[i]))
        print("")
        return True
    for c in range(n):
        if c in col or r+c in d1 or r-c in d2:
            continue
        
        sol[r][c]="Q"
        col.add(c)
        d1.add(r+c)
        d2.add(r-c)
        if backtrack(r+1):
            return True

        sol[r][c]='.'
        col.remove(c)
        d1.remove(r+c)
        d2.remove(r-c)
    return False
backtrack(0)"""



# all the possible path
n=4
sol=[['.']*n for _ in range(n)]
col=set()
d1=set()
d2=set()

def backtrack(r):
    if r==n:
        for i in range(n):
            print("".join(sol[i]))
        print("")
        return
    for c in range(n):
        if c in col or r+c in d1 or r-c in d2:
            continue
        
        sol[r][c]="Q"
        col.add(c)
        d1.add(r+c)
        d2.add(r-c)
        backtrack(r+1)


        sol[r][c]='.'
        col.remove(c)
        d1.remove(r+c)
        d2.remove(r-c)
backtrack(0)