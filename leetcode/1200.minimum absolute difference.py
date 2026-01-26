
class Solution:
    def minimumAbsDifference(self, a):
        a.sort()
        d=[a[i+1]-a[i] for i in range(len(a)-1)]
        target=min(d)
        res=[]
        for i,diff in enumerate(d):
            if diff==target:
                res.append([a[i],a[i+1]])
        return res
obj=Solution()
print(obj.minimumAbsDifference([4,2,1,3]))