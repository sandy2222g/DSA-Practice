class Solution:
    def concatenatedBinary(self, n: int) -> int:
        s=[]
        for i in range(1,n+1):
            s.append(bin(i)[2:])
        return int("".join(s),2)%(10**9+7)
obj=Solution()
print(obj.concatenatedBinary(12))