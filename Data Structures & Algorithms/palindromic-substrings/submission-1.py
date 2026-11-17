# Plan :
# 1. Find Odd length palindrome
# L = i ; R = i 
# 2. Find even length palindrome
# L = i ; R = i + 1
# Total = Odd to even
# Time complexity: O(n) Space: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0 
        # Even
        for i in range(len(s)):
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        # Odd
        for i in range(len(s)):
            l,r = i,i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res