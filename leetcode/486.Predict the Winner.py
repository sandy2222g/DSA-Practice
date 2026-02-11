
class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        @lru_cache(None)
        def dfs(l,r):
            if l==r:
                return nums[l]
            lef=nums[l]-dfs(l+1,r)
            re=nums[r]-dfs(l,r-1)
            return max(lef,re)
        return dfs(0,len(nums)-1)>=0