class Solution:
    def minOperations(self, s: str) -> int:
        c=0
        for i in range(len(s)):
            if i%2:
                if s[i]=='0':
                    c+=1
            else:
                if s[i]=='1':
                    c+=1
        return min(c,len(s)-c)
obj=Solution()
print(obj.minOperations('01100'))