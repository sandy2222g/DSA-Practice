class Solution:
    def minRemoval(self, nums: list[int], k: int) -> int:
        nums.sort()
        c=0
        i=0
        j=0
        while j<len(nums):
            if nums[i]*k>=nums[j]:
                c=max(c,j-i+1)
                j+=1
            else:
                i+=1
        return len(nums)-c

obj=Solution()
print(obj.minRemoval([2,1,5],2))