class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        c=0
        for i in data:
            if c==0:
                
                if i>>5 == 0b110:
                    c=1
                elif i>>4 == 0b1110:
                    c=2
                elif i>>3 == 0b11110:
                    c=3
                elif i>>7 != 0b0:
                    return False
            else:
                if i>>6 !=0b10:
                    return False
                c-=1
        return c==0
obj=Solution()
print(obj.validUtf8([197,130,1]))