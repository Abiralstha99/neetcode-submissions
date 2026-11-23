# bottom-up
# dp[i] = Number of ways to decode the first i character
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2,len(s)+1):
            oneDigit = int(s[i-1:i])
            twoDigit = int(s[i-2:i])
            if (oneDigit >= 1):
                dp[i] += dp[i-1]
            
            if (twoDigit >= 10 and twoDigit <= 26):
                dp[i] += dp[i - 2]
        return dp[-1]
                
                

        
