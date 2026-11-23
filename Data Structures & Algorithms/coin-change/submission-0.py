# dp[i] = min coins to make i 
# dp[i] = dp[i - c] + 1 and i >= c to consider c
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            if i in coins:
                dp[i] = 1
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i],(dp[i - coin] + 1))
        return -1 if dp[amount] == float('inf') else dp[amount]