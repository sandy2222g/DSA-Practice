class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        ans = 0
        sign = 1
        for ch in s:
            ans += sign * (ord(ch) - 48)
            sign *= -1
        return ans
obj=Solution()
print(obj.alternateDigitSum(521))