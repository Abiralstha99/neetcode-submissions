# plan 
# 1. dp[i] = if the string is of length i, would that be solved

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        wordSet = set(wordDict)

        # Calculate the max len of words
        maxLen = 0
        for word in wordSet:
            maxLen = max(maxLen, len(word))
        
        dp[0] = True

        for i in range(1,len(dp)):
            # For each chracter go back atmost maxLen
            for j in range(i, max(0,i - maxLen) - 1,-1):
                if s[j:i] in wordSet and dp[j]:
                    dp[i] = True
                    break
        return dp[-1]