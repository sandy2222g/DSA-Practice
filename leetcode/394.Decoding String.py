class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        for i in s:
        
            if i!=']':
                st.append(i)
            else:
                k=''
                while st[-1]!="[":
                    k=st.pop()+k
                st.pop()
                n=''
                while st and st[-1].isdigit():
                    n=st.pop()+n
                if n:
                    st.append(int(n)*k)
        return "".join(st)