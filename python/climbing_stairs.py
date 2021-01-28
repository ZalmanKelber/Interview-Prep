class Solution:
    def climbStairs(self, n: int) -> int:
        memo = { n - 1: 1, n - 2: 2 }
        def backtrack(step) -> int:
            if step not in memo:
                memo[step] = backtrack(step + 1) + backtrack(step + 2)
            return memo[step]
        return backtrack(0)