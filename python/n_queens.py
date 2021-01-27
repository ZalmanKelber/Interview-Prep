class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #solutions will be in the form of a list of column indices corresponding to 
        #each row
        self.n = n
        self.solutions = []
        self.stack = []
        self.backtrack()
        return [self.draw_solution(sol) for sol in self.solutions]
    
    def backtrack(self) -> None:
        if len(self.stack) == self.n:
            self.solutions.append(self.stack[:])
            return 
        for i in range(self.n):
            if self.is_valid(i):
                self.stack.append(i)
                self.backtrack()
                self.stack.pop()
    
    def is_valid(self, col: int) -> bool:
        for i, val in enumerate(self.stack):
            if val == col or abs(len(self.stack) - i) == abs(col - val):
                return False
        return True
    
    def draw_solution(self, sol: List[int]) -> List[str]:
        image = []
        for row in sol:
            row_string = []
            for i in range(self.n):
                row_string.append("." if i != row else "Q")
            image.append("".join(row_string))
        return image