class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1 = [-1] * len(nums)
        dp2 = [-1] * len(nums)
        if len(nums) == 0:
                return 0 
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        
        def dfs(start,end,dp):
            if start > end:
                return 0
            if dp[start] != -1:
                return dp[start]
            dp[start] = max(nums[start] + dfs(start+2,end,dp), dfs(start+1,end,dp))
            return dp[start]
        return max(dfs(0,len(nums) - 2,dp1),dfs(1,len(nums) - 1,dp2))
            

        
        