class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        target = len(cost)
        dp = [-1] * (target + 1)
        # start = current index
        def min_cost(start):
            if start >= target:
                return 0
            
            if dp[start] != - 1:
                return dp[start]
            dp[start] = cost[start] + min(min_cost(start + 1),min_cost(start + 2))
            return dp[start]
        
        res = min(min_cost(0), min_cost(1))
        return res