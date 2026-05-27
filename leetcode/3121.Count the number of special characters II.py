from collections import defaultdict
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        dd=defaultdict(int)
        d=defaultdict(int)
        for i,v in enumerate(word):
            if v.islower():
                dd[v]=i
            elif v not in d:
                d[v]=i
        c=0
        for i,x in dd.items():
            ii=i.upper()
            if ii in d and d[ii]>x:
                c+=1
        return c

obj=Solution()
print(obj.numberOfSpecialChars("aaAbcBC"))