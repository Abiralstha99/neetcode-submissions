'''
Time complexity : o(n)
Space : O(n)
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))