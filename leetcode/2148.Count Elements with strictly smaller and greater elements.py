class Solution:
    def countElements(self, nums: list[int]) -> int:
        c=0
        a,b=min(nums),max(nums)
        for i in nums:
            if a<i<b:
                c+=1
        return c
obj=Solution()
print(obj.countElements([11,7,2,15]))