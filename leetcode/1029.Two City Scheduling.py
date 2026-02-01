class Solution:
    def twoCitySchedCost(self, costs):
        costs.sort(key=lambda x: x[0] - x[1])
        n=len(costs)//2
        t=0
        for i in range(len(costs)):
            if i<n:
                t+=costs[i][0]
            else:
                t+=costs[i][1]
        return t
obj=Solution()
print(obj.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))