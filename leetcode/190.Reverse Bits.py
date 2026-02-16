class Solution:
    def reverseBits(self, n: int) -> int:
        return(int(bin(n)[2:].zfill(32)[::-1],2))
        return 0
obj=Solution()
print(obj.reverseBits(43261596))