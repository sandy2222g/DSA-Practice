class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        nums[1:]=sorted(nums[1:])
        return nums[0]+nums[1]+nums[2]
obj=Solution()
print(obj.minimumCost([1,2,3,12]))