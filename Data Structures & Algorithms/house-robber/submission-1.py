# memoization
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        def rob_max(house):
            if house >= len(nums):
                return 0
            # Check if it already exist in the array
            if dp[house] != -1:
                return dp[house]
            dp[house] = max(rob_max(house + 1), nums[house] + rob_max(house + 2))
            return dp[house]
        return rob_max(0)