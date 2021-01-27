class Solution {
    
    int[] nums = new int[0];
    List<List<Integer>> solutions = new ArrayList();
    Set<Integer> unusedIndices = new HashSet();
    Stack<Integer> stack = new Stack();
    
    public List<List<Integer>> permute(int[] nums) {
        this.nums = nums;
        for (int i = 0; i < nums.length; i++) {
            unusedIndices.add(i);
        }
        backtrack();
        return solutions;
    }
    
    private void backtrack() {
        if (unusedIndices.size() == 0) {
            List<Integer> sol = new ArrayList();
            for (int num : stack) {
                sol.add(num);
            }
            solutions.add(sol);
            return;
        }
        for (int index : new HashSet<Integer>(unusedIndices)) {
            stack.push(nums[index]);
            unusedIndices.remove(index);
            backtrack();
            unusedIndices.add(index);
            stack.pop();
        }
    }
}