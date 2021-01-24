class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #set the grid to an instance variable
        self._grid = grid
        #add the recursive base class to the memo
        self._memo = { (len(grid) - 1, len(grid[0]) - 1): grid[len(grid) - 1][len(grid[0]) - 1] }
        return self.recursive_min_path_sum(0, 0)
        
    def recursive_min_path_sum(self, row: int, col: int) -> int:
        #check if problem is in memo
        if (row, col) not in self._memo:
            #add the current square to the result
            result = self._grid[row][col]
            #collect the possible sub problems and find the minimum and add it to the result
            sub_problems = []
            if row < len(self._grid) - 1:
                sub_problems.append(self.recursive_min_path_sum(row + 1, col))
            if col < len(self._grid[0]) - 1:
                sub_problems.append(self.recursive_min_path_sum(row, col + 1))
            result += min(sub_problems)
            #add result to memo
            self._memo[(row, col)] = result
        return self._memo[(row, col)]