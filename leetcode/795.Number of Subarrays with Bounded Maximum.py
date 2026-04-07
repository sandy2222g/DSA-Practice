class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        s=e=-1
        r=0
        for i in range(len(nums)):
            if nums[i]>right:
                s=e=i
            elif nums[i]>=left:
                e=i
            r+=e-s
        return r
obj=Solution()
print(obj.numSubarrayBoundedMax([2,1,4,3],2,3))