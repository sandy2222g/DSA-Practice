class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s
obj=Solution()
print(obj.checkOnesSegment('110'))