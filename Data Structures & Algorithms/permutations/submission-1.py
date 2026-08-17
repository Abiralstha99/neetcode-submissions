class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        Understand: 
        input: list of nums
        output: different ways of choosing

        choose the number you haven't choosed yet

        Plan:
        base case : if len(cur) == len(nums):
        add to the result

        use a boolean use array that marks which element is used or      which is not 

        '''

        res, curr, used = [], [], len(nums)*[False]
        def dfs(i, curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return 
            
            for j in range(len(nums)): 
                # Append if not present in used
                if used[j]: 
                    continue
                else:
                    curr.append(nums[j])
                    used[j] = True
                    dfs(j + 1, curr)

                    # To backtrack now pop
                    curr.pop()
                    used[j] = False
        dfs(0,curr)
        return res



