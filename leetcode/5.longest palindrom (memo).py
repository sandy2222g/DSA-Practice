from functools import lru_cache
class Solution:
    @lru_cache(None)
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        left = self.longestPalindrome(s[1:])
        right = self.longestPalindrome(s[:-1])

        return left if len(left) > len(right) else right
