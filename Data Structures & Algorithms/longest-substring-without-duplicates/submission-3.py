class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        right = 0
        substring = set()
        res = 0
        while (right < len(s)):
            # Check if the char is in the set
            while (s[right] in substring):
                substring.remove(s[left])
                left += 1
            substring.add(s[right])
            res = max(res,right - left + 1)
            right += 1
        return res

