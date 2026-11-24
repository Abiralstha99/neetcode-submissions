class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        left = 1
        right = 1
        res = nums[0]
        for i in range(len(nums)):
            left *= nums[i]
            right *= nums[- 1 - i]
            res = max(res,left,right)

            if left == 0:
                left = 1
            if right == 0:
                right = 1
        return res