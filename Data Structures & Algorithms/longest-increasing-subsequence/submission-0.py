# DP[i] = longest increasing subsequence ending at nums[i]
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums))
        maxLIS = -1
        for i in range(1,len(nums)):
            for j in range(i - 1,-1,-1):
                # On going back I need to validate it's value smaller and largest dp
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)