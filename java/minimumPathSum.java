class Solution {
    //store the grid as an instance variable
    private int[][] grid;
    //store memo as a map that maps columns onto maps that map row onto subproblem result
    private Map<Integer, Map<Integer, Integer>> memo = new HashMap<>();

    public int minPathSum(int[][] grid) {
        this.grid = grid;
        //add recursive base case to memo
        Map<Integer, Integer> baseCase = new HashMap<>();
        baseCase.put(grid[0].length - 1, grid[grid.length - 1][grid[0].length - 1]);
        memo.put(grid.length - 1, baseCase);
        return recursiveMinPathSum(0, 0);
    }
    
    private int recursiveMinPathSum(int row, int col) {
        //check if problem is in memo
        if (!memo.keySet().contains(row) || !memo.get(row).keySet().contains(col)) {
            //add the current grid to the result
            int result = grid[row][col];
            //add the possible subproblems to a list and add the smallest one to the result
            List<Integer> subProblems = new ArrayList<>();
            if (row < grid.length - 1) {
                subProblems.add(recursiveMinPathSum(row + 1, col));
            }
            if (col < grid[0].length - 1) {
                subProblems.add(recursiveMinPathSum(row, col + 1));
            }
            Collections.sort(subProblems);
            result += subProblems.get(0);
            //add the result to the memo
            if (!memo.keySet().contains(row)) {
                memo.put(row, new HashMap<Integer, Integer>());
            }
            memo.get(row).put(col, result);
        }
        return memo.get(row).get(col);
    }
    
}