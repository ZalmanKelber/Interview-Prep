class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.solutions = []
        self.stack = []
        self.open_paren_count = 0
        self.closed_paren_count = 0
        self.n = n
        self.backtrack()
        return self.solutions
    
    def backtrack(self) -> None:
        if len(self.stack) == 2 * self.n:
            self.solutions.append("".join(self.stack))
            return
        if self.closed_paren_count < self.open_paren_count:
            self.closed_paren_count += 1
            self.stack.append(")")
            self.backtrack()
            self.stack.pop()
            self.closed_paren_count -= 1
        if self.open_paren_count < self.n:
            self.open_paren_count += 1
            self.stack.append("(")
            self.backtrack()
            self.stack.pop()
            self.open_paren_count -= 1