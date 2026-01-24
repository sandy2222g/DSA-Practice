from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r=[]
        s=[]
        def backtrack(i=0): 
            if i==len(nums):
                r.append(s.copy())
                return
            s.append(nums[i])
            backtrack(i+1)
            s.pop()
            backtrack(i+1)
        backtrack()
        return r
obj=Solution()
print(obj.subsets([1,2,3]))