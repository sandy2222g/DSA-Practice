from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        vis=set()
        s=[]
        r=[]
        def bt(i=0):
            if i==len(nums):
                t=tuple(sorted(s))
                if t not in vis:
                    r.append(list(t))
                    vis.add(t)
                return 
            s.append(nums[i])
            bt(i+1)
            s.pop()
            bt(i+1)
        bt()
        return r
obj=Solution()
print(obj.subsetsWithDup([1,2,2]))