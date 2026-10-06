class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [-1] * (n + 1)
        def climb(n):
            if arr[n] != -1:
                return arr[n]
            elif n == 1:
                return 1
            elif n == 2:
                return 2
            arr[n] = climb(n-1) + climb(n-2)
            return arr[n]
        return climb(n)
