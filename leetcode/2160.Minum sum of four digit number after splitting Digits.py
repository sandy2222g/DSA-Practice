class Solution:
    def minimumSum(self, num: int) -> int:
        d=sorted(map(int,str(num)))
        a=d[0]*10+d[2]
        b=d[1]*10+d[3]
        return a+b
obj=Solution()
print(obj.minimumSum(2932))