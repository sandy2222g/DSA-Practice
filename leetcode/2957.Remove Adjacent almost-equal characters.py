class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        s=[]
        c=0
        for i in word:
            if not s:
                s.append(i)
            elif abs(ord(s[0])-ord(i))>=2:
                s[0]=i
            else:
                s.pop()
                c+=1
        return c
obj=Solution()
print(obj.removeAlmostEqualCharacters("qawezryxstcvkbuoliujyhtersdxcfvgyuhoili"))