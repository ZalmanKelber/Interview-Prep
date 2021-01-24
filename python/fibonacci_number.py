class Solution:
    #store recursive base cases in the cache
    memo = { 0: 0, 1: 1 }
    def fib(self, n: int) -> int:
        #check if problem is already in cache
        if n in self.memo:
            return self.memo[n]
        #otherwise get solution recursively and store it in cache
        result = self.fib(n - 1) + self.fib(n - 2)
        self.memo[n] = result
        return result