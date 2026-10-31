# Bottom up 
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Cause 0-based array
        target = len(cost) + 1
        arr = [-1] * (target)
        arr[0] = 0
        arr[1] = 0
        
        for i in range(2, target):
            arr[i] = min (arr[i - 1] + cost[i-1], arr[i -2] + cost[i - 2])
        return arr[len(cost)]
            
