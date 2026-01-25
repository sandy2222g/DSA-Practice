from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        r=[]
        def backtrack(c=[]):
            if len(c)==len(nums):
                r.append(c.copy())
            for i in nums:
                if i in c:
                    continue
                c.append(i)
                backtrack(c)
                c.pop()
        backtrack()
        return r
obj=Solution()
print(obj.permute([1,2,3]))