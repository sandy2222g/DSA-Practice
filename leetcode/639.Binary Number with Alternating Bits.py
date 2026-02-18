class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        k=n^n>>1
        return (k+1)&k==0
            
obj=Solution()
print(obj.hasAlternatingBits(11))