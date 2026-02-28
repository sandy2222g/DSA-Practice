class Solution:
    def maxGoodNumber(self, nums: list[int]) -> int:
        s=[bin(i)[2:] for i in nums]
        s.sort(reverse=True,key=lambda x:x*10)
        print(s)
        return int("".join(s),2)
obj=Solution()
print(obj.maxGoodNumber([1,2,3]))