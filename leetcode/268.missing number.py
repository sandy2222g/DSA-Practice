class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return n*(n+1)//2 - sum(nums)
obj=Solution()
print(obj.missingNumber([3,0,1]))