from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        d=defaultdict(list)
        r=[]
        for i,x in enumerate(groupSizes):
            d[x].append(i)
            if len(d[x])==x:
                r.append(d[x])
                d[x]=[]
        
        return r
obj=Solution()
print(obj.groupThePeople([2,3,3,3,2,1]))