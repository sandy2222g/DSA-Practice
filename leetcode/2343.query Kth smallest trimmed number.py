class Solution:
    def smallestTrimmedNumbers(self, nums: list[str], queries: list[list[int]]) -> list[int]:
        res = []
        for place,trim in queries:
            tempnums=[]
            for i in range(len(nums)):
                tempnums.append((nums[i][-trim:],i))
            tempnums.sort()
            res.append(tempnums[place-1][1])
        return res
obj=Solution()
print(obj.smallestTrimmedNumbers(["102","473","251","814"],[[1,1],[2,3],[4,2],[1,2]]))