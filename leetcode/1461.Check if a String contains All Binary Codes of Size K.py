class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        r=set()
        for i in range(len(s)-k+1):
            if s[i:k+1] not in r:
                r.add(s[i:i+k])    
        return len(r)==2**k
obj=Solution()
print(obj.hasAllCodes("00110110",2))