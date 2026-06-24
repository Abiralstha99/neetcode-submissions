class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        l = 0
        for r in range(len(prices)):
            while (prices[r] < prices[l]):
                # minimize the window 
                l += 1
            else:
                # increase the window 
                # update the profit 
                profit = max(profit,prices[r] - prices[l])
        return profit