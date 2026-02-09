class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        r=sum(nums[:k])
        a=r/k
        for i in range(k,len(nums)):
            r+=nums[i]
            r-=nums[i-k]
            a=max(a,r/k)
        return a
obj=Solution()
print(obj.findMaxAverage([1,12,-5,-6,50,3],4))