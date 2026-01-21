from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        r=[]
        def bt(c=[],i=1):
            if len(c)==k:
                r.append(c.copy())
                return False
            if i>n:
                return False
            for j in range(i,n+1):
                c.append(j)
                bt(c,j+1)
                c.pop()
        bt()
        return r
obj=Solution()
print(obj.combine(int(input()),int(input())))