class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        input: list of nums
        output: permutation 

        base case:
        if len(nums) == len(curr):
            return

        # choose the number you haven't choosen yet. 
        '''
        res, curr = [], []
        used = len(nums) * [False]
        def dfs(i):
            if (len(nums) == len(curr)):
                res.append(curr.copy())
                return

            for j in range(len(nums)): 
                if used[j]:
                    continue
                else:
                    curr.append(nums[j])
                    used[j] = True
                    dfs(j + 1)
                    curr.pop()
                    used[j] = False
        dfs(0)
        return res
            

        