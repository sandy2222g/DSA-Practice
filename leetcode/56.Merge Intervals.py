class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda interval: interval[0])
        l=[]
        for i in intervals:
            if not l or l[-1][1]<i[0] :
                l.append(i)
            else:
                l[-1][1]=max(i[1],l[-1][-1])
        return l
obj=Solution()
print(obj.merge([[1,3],[2,6],[8,10],[15,18]]))