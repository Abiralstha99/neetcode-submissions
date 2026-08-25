class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        input: int n 
        output: return list of parenthesis string 

        match: backtracking, stack

        plan: 
        1. You have 2 choices: ( or )
        2. You can only choose a ) if you already have a (
        3. If open < n : choose open 
        4. If close < open: choose close
        5. if open == close == n ; then add to res
        '''

        res = []
        curr = ""
        def dfs(open,close, curr):
            if open == n and close == n: 
                res.append(curr)
                return 
            if open < n:
                curr = curr + "("
                dfs(open + 1, close, curr)
                curr = curr[:-1]
            if close < open: 
                curr = curr + ")"
                dfs(open, close + 1, curr)
        dfs(0,0, curr)
        return res