class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]
obj=Solution()
print(obj.addBinary("1010","1110"))