class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n = n
        self.k = k
        self.solutions = []
        self.stack = []
        self.backtrack()
        return self.solutions
    
    def backtrack(self) -> None:
        if len(self.stack) == self.k:
            self.solutions.append(self.stack[:])
            return
        start_value = 1 if len(self.stack) == 0 else self.stack[-1] + 1
        for num in range(start_value, self.n + 1 - (self.k - 1 - len(self.stack))):
            self.stack.append(num)
            self.backtrack()
            self.stack.pop()