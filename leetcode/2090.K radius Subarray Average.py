class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        dp=[-1]*len(nums)
        dd=k*2+1
        for i in range(k,len(nums)-k):
            if i==k:
                s=sum(nums[i-k:i+k+1])
                dp[i]=s//dd
            else:
                s+=nums[i+k]
                s-=nums[i-k-1]
                dp[i]=s//dd
        return dp
obj=Solution()
print(obj.getAverages([7,4,3,9,1,8,5,2,6],3))