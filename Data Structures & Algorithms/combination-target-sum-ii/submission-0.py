class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        Input : list of nums containing duplicates, target
        Output: combination set that sums to target

        Plan: 
        1. Sort the array and use while i == i + 1, skip to avoid duplication 
        2. Base case if sum > target, return
        3. if sum == target, return 
        '''

        res, cur = [], []
        candidates.sort()
        n = len(candidates)
        # 
        def dfs(i, total):
            if total == target:
                res.append(cur.copy())
                return 
            if total > target or i == n:
                return 
            
            #  include candidates[i]
            cur.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            cur.pop()

            # Not include the same 
            while i + 1 < n and candidates[i] == candidates[i +1]:
                i += 1
            dfs(i + 1, total)
        dfs(0,0)
        return res