class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        last_square = (len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)
        if obstacleGrid[last_square[0]][last_square[1]] != 0 or obstacleGrid[0][0] != 0:
            return 0
        memo = { last_square: 1 }
        def backtrack(location: Tuple[int, int]) -> int:
            if location not in memo:
                subProblems = []
                x, y = location
                if x + 1 < len(obstacleGrid) and obstacleGrid[x + 1][y] == 0:
                    subProblems.append(backtrack((x + 1, y)))
                if y + 1 < len(obstacleGrid[0]) and obstacleGrid[x][y + 1] == 0:
                    subProblems.append(backtrack((x, y + 1)))
                memo[location] = sum(subProblems)
            return memo[location]
        return backtrack((0, 0))