adjacents = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.grid = grid;
        self.empty_squares = sum([sum([1 if cell == 0 else 0 for cell in row]) for row in grid])
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    self.starting_square = (i, j)
                if cell == 2:
                    self.ending_square = (i, j)
        self.stack = [self.starting_square]
        self.found_squares = set()
        self.num_solutions = 0
        self.backtrack()
        return self.num_solutions
    
    def backtrack(self) -> None:
        if len(self.stack) == self.empty_squares + 1:
            for adj in adjacents:
                if (self.stack[-1][0] + adj[0], self.stack[-1][1] + adj[1]) == self.ending_square:
                    self.num_solutions += 1
            return
        for adj in adjacents:
            next_square = (self.stack[-1][0] + adj[0], self.stack[-1][1] + adj[1])
            if self.is_valid(next_square):
                self.stack.append(next_square)
                self.found_squares.add(next_square)
                self.backtrack()
                self.found_squares.remove(self.stack.pop())
                
    def is_valid(self, next_square: Tuple[int, int]) -> bool:
        if next_square in self.found_squares:
            return False
        if not 0 <= next_square[0] < len(self.grid):
            return False
        if not 0 <= next_square[1] < len(self.grid[0]):
            return False
        if self.grid[next_square[0]][next_square[1]] != 0:
            return False
        return True