class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        # size of the window
        count = 0
        res = set()
        for r in range(len(s)):
            while s[r] in res:
                # remove the 
                res.remove(s[l])
                l += 1
            res.add(s[r])
            count = max(count, r - l + 1)
        return count

            