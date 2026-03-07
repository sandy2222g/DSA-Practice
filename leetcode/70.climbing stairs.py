class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3: return n
        c=0
        p=3
        s=2
        for i in range(3,n):
            c=p+s
            s=p
            p=c
        return c
obj=Solution()
print(obj.climbStairs(24))