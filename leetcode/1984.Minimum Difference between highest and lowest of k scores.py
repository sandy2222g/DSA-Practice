from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=float('inf')
        j=k-1
        for i in range(len(nums)-j):
            ans=min(ans,nums[i+j]-nums[i])
        return ans
obj=Solution()
print(obj.minimumDifference([9,4,1,7],2))