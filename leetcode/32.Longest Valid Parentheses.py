class Solution:
    def longestValidParentheses(self, st: str) -> int:
        stack=[-1]
        l=0
        for i in range(len(st)):
            if st[i] =='(':
                stack.append(i)
            else:
                stack.pop()
                if  not stack:
                    stack.append(i)
                else:
                    l=max(l,i-stack[-1])
        return l
obj=Solution()
print(obj.longestValidParentheses('(()()())))'))