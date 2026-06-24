class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Plan : 
        # 1. Create prefix and suffix array 
        # 2. Then, multiply while appending

        res = []
        # Creating prefix array and appending 
        prefix = 1
        for i in range(0,len(nums)):
            res.append(prefix)
            prefix *= nums[i]
        
        suffix = 1
        # Creating suffix array and appending 
        for i in range(len(nums) - 1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
        

            
