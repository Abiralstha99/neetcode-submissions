# Plan;
# 1. Prefix and suffix product 
# 2. If encounter 0, record 0 and then change it to 1 to avoid the product being 0 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        left = 1
        right = 1
        res = nums[0]
        for i in range(len(nums)):
            left *= nums[i]
            right *= nums[- 1 - i]
            res = max(res,left,right)
            left = left or 1
            right = right or 1
        return res