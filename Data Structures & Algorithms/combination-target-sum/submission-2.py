class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        Input : list of numbers, target
        Output : [[]] st sum = target 

        Match : Dfs backtracking 
        Plan: 
        Base case 
        if i >= len(nums):
            append the combination to res
            return 
        
        Choose yourself or either choose the next number
        '''

        res, sol = [], []
        nums.sort()
        n = len(nums)
        def dfs(i, total):
            if total == target:
                res.append(sol.copy())
                return 
            if total > target:
                return
            # Try each possible next number
            for j in range(i,n):
                sol.append(nums[j])
                dfs(j, total + nums[j])
                sol.pop()

        dfs(0, 0)
        return res

        