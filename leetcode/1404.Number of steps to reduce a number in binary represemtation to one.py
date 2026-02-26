class Solution:
    def numSteps(self, s: str) -> int:
        c=0
        n=int(s,2)
        while n!=1:
            if n%2==0:
                n//=2
            else:
                n+=1
            c+=1
        return c
obj=Solution()
print(obj.numSteps('11011'))