class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        arr.sort(key=lambda x : [x.bit_count(),x])
        return arr
obj=Solution()
print(obj.sortByBits([0,1,2,3,4,5,6,7,8]))