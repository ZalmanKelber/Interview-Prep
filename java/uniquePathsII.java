class Solution {
    
    Map<Integer, Map<Integer, Integer>> memo = new HashMap();
    int n = 0;
    int m = 0;
    int[][] obstacleGrid = new int[0][0];
    int curX = 0;
    int curY = 0;
    
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        n = obstacleGrid.length;
        m = obstacleGrid[0].length;
        if (obstacleGrid[n - 1][m - 1] != 0 || obstacleGrid[0][0] != 0) {
            return 0;
        }
        this.obstacleGrid = obstacleGrid;
        Map<Integer, Integer> lastKey = new HashMap();
        lastKey.put(m - 1, 1);
        memo.put(n - 1, lastKey);
        return backtrack();
    }
    
    private int backtrack() {
        if (!memo.keySet().contains(curX) || !memo.get(curX).keySet().contains(curY)) {
            curX++;
            int leftSubproblem = curX < n && obstacleGrid[curX][curY] == 0 ? backtrack() : 0;
            curX--;
            curY++;
            int rightSubproblem = curY < m && obstacleGrid[curX][curY] == 0 ? backtrack() : 0;
            curY--;
            int result = leftSubproblem + rightSubproblem;
            if (memo.keySet().contains(curX)) {
                memo.get(curX).put(curY, result);
            } else {
                Map<Integer, Integer> curKey = new HashMap();
                curKey.put(curY, result);
                memo.put(curX, curKey);
            }
        }
        return memo.get(curX).get(curY);
    }
}