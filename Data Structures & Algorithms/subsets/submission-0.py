class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        n = len(nums)
        def backtrack(i):
            # Base condtion:
            if i >= n:
                res.append(subset.copy())
                return 
            
            # Decision 1 : Choose the number 
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()

            # Decision 2: Skip the number 
            backtrack(i + 1)
        backtrack(0)
        return res
