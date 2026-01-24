class Solution:
    def totalNQueens(self, n: int) -> int:
        sol=[['.']*n for _ in range(n)]
        count=0
        col=set()
        d1=set()
        d2=set()
        def bt(r):
            if r==n:
                nonlocal count
                count+=1
                return 
            for c in range(n):
                if c in col or r+c in d1 or r-c in d2:
                    continue
                sol[r][c]="Q"
                col.add(c)
                d1.add(r+c)
                d2.add(r-c)
                bt(r+1)

                sol[r][c]="."
                col.remove(c)
                d1.remove(r+c)
                d2.remove(r-c)
        bt(0)
        return count
obj=Solution()
print(obj.totalNQueens(8))
