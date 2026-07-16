class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0 
        dict = {}
        res = 0 
        for right in range(0,len(s)):
            dict[s[right]] = dict.get(s[right],0) + 1
            window_length = right - left + 1
            freq = max(dict.values())
            # if the window is invalid
            if (window_length - freq > k):
                dict[s[left]] -= 1
                left += 1
                window_length -= 1
            res = max(res, window_length)
        return res
            