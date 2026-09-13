'''
Plan: 
1. Take prefix product and suffix product 
2. Then multiply
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        # prefix product
        for i in range(len(nums)):
            res.append(prefix)
            prefix *= nums[i]
        
        # res = [1,1,2,8]

        # suffix product - go from last
        suffix = 1
        for i in range(len(nums) -1,-1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
        
        
