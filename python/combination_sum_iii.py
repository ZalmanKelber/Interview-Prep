class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.k = k
        self.n = n
        self.stack = []
        self.cur_sum = 0
        self.solutions = []
        self.backtrack()
        return self.solutions
    
    def backtrack(self) -> None:
        if len(self.stack) == self.k:
            if self.cur_sum == self.n:
                self.solutions.append(self.stack[:])
            return 
        for num in range(self.stack[-1] + 1 if len(self.stack) > 0 else 1, min((self.n - self.cur_sum) // (self.k - len(self.stack)) + 1, 10)):
            self.stack.append(num)
            self.cur_sum += num
            self.backtrack()
            self.cur_sum -= num
            self.stack.pop()