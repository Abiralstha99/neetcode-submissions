class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,0
        profit = 0
        while (r < len(prices)):
            # Compare to see if it's profitable
            if (prices[r] > prices[l]):
                profit = max(profit, prices[r]-prices[l])
                r += 1
            else:
                # If it's a loss
                l = r
                r += 1
        return profit
            
            